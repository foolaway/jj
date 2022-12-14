#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import configparser
import getpass
import os
import platform

from libcore.exception.get_system_onfo_exception import GetSystemInfoException
from libcore.exception.not_support_system_type_exception import NotSuppotSytemTypeException
from libcore.util.string_util import StringUtil

from libcore.exception.config_key_not_exist_exception import ConfigKeyNotExistException, ConfigKeyNotExistException


class Config:
    """
    配置
    """
    __init_system_info = None
    __init_system_info = None
    __default_mirror = None
    __default_lang = "en_US"
    __default_publisher = "Oracle"

    __config = ""

    __config_file_windows_tpl = "{system_root}\\User\\{username}\\AppData\\local\\jjvmm\\config\\.jjvmm-config.ini"
    __config_file_osx_tpl = "/Users/{username}/.jjvmm/config/.jjjvmm-config.ini"
    __config_file_Linux_tpl = "/home/{Username}/.jjvmm/config/.jjvmm-config.ini"

    __config_file_windows = None
    __config_file_Linux = None
    __config_file_osx = None

    __curr_system_type = None
    __curr_windows_system_root = "C:"
    __curr_username = None

    __allow_config_keys = (
        'mirror',
        'lang',
        'publisher'
    )

    def __init_system_info(self):
        """
        获取操作系统各种信息
        :return:
        """

        # 获得操作系统版本
        system_type = platform.system()
        # 返回你当前系统的用户名,,,而而getpass.getpass()就是主要用途提示用户输入密码
        curr_username = getpass.getuser()

        if StringUtil.is_empty(curr_username):
            raise GetSystemInfoException("Failed to get current user name.")

        # strip() 方法用于删除字符串头部和尾部指定的字符，默认字符为所有空字符，包括空格、换行(\n)、制表符(\t)等。
        self.__curr_username = curr_username.strip()

        if system_type == "Darwin":
            # 将用户名传参初始化
            self.__curr_system_type = "OSX"
            return system_type
        elif system_type == "Windows":
            # 获取系统盘位置
            system_root = os.getenv("SystemDrive", default="C:")
            if StringUtil.is_empty(system_root):
                raise GetSystemInfoException("Illegal system root path: {}".format(system_root))

            self.__curr_windows_system_root = system_root.strip()
            return system_root

        elif system_type == "Linux":
            self.__curr_system_type = "Linux"
            return system_type
        else:
            raise NotSuppotSytemTypeException("Unrecognized operating system.")

    def __init__config_file_location(self):
        """
        初始化配置文件位置
        :return:
        """
        if self.__curr_system_ytpe == "OSX":
            self.__config_file_osx = self.__config_file_osx_tpl.format(username=self.__curr_username)
            return self.__config_file_osx
        elif self.__curr_system_type == "Windows":
            self.__config_file_windows = self.__config_file_windows_tpl.format(system_root=self.__system_root,
                                                                               usrname=self.__curr_username)
            return self.__config_file_windows
        elif self.__curr_system_type == "Linux":
            self.__config_file_Linux = self.__config_file_Linux_tpl.format(username=self.__curr_username)
            return self.__config_file_Linux
        else:
            pass

    def __load_config_file(self):
        """
        加载配置问渐渐
        如果文件不存在，那么不加载
        如果第一次保持配置的时候，文件不存在，直接创建
        如果纹在操作，加载，修改
        :return:
        """
        # TOO 通过操作系统路径加载，jjvmm-config.init
        filename = ""
        if os.path.exists(filename):
            self.__config = configparser.ConfigParser()
            self.__config.read(filename, encoding="UTF-8")

            sections = self.__config.sections()
            if "app" not in sections:
                raise ConfigKeyNotExistException(filename)

    def __init__(self):
        self.__init_system_info()
        self.__init__config_file()
        self.__load_config_file()

    def get(self, key: str) -> str:

        """
        获取配置项
        :param key: key
        :return: Value
        """

        if StringUtil.is_empty(key):
            raise ConfigKeyNotExistException("{} is not in config file.because key is empty".format(key))

        if key not in self.__allow_config_keys:
            raise ConfigKeyNotExistException("{} is not in config file.".format(key))

        key = key.strip()
        if self.__config is None:
            return self.__match_config_key()

        else:
            val = self.__config.get("app", key).strip()
            return self.__match_config_key(key=key) if StringUtil.is_empty(val) else val

    def __match_config_key(self, key: str) -> str:
        if key == "mirror":
            return self.__default_mirror
        elif key == "lang":
            return self.__default_lang
        elif key == "publisher":
            return self.__default_publisher

    def set(self, key: str, value: str):
        """
        设置配置项
        :param key: key
        :param value: Value
        :return: 如果不存在这个配置项，那么返回 False
        """
        config = configparser.RawConfigParser()
        file_path = self.__init__config_file_location()
        config.read(file_path)
        config.set(key, value)

        if StringUtil.is_empty(key):
            raise ConfigKeyNotExistException("{} is not in config file.because key is empty".format(key))

        if key not in self.__allow_config_keys:
            return False

        else:
            dict[key] = value

    def get_with_default(self, key: str, default: str):

        """
        获取配置项，如果这个配置项的值为空，那么返回用户的 default
        :param key: key
        :return: Value
        :param  default：默认值
        :return:Value
        """

        if StringUtil.is_empty(key):
            raise ConfigKeyNotExistException("{} is not in config file.because key is empty".format(key))

        if key not in self.__allow_config_keys:
            return False


if __name__ == '__main__':
    pass
