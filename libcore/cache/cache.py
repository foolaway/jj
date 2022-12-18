#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import datetime
import getpass
import os
import platform
import time

from libcore.config.config import Config
from libcore.exception.cached_file_does_not_exist import CachedFileDoesNotExist
from libcore.exception.not_support_system_type_exception import NotSuppotSytemTypeException


class Cache:
    """
    缓存
    """

    __file_ext = ".store"

    # __cache_name_tpl = "{fileid}###{year}#{month}#{day}{file_ext}"

    __cache_file_windows_tpl = "{SystemRoot}\\ProgramData\\jjvmm\\cache\\"

    __cache_file_path = None

    #   判断系统
    @staticmethod
    def __init__system_type():
        system_type = platform.system()
        if system_type == "Linux":
            Cache.__cache_file_path = " /usr/local/jjvmm/Cache/"
        elif system_type == "Darwin":
            Cache.__cache_file_path = "/usr/local/jjvmm/Cache/"
        elif system_type == "Windows":
            system_root = os.getenv("SystemDrive", default="C")

            Cache.__cache_file_path = Cache.__cache_file_windows_tpl.format(SystemRoot=system_root)

        else:
            raise NotSuppotSytemTypeException("Unrecognized operating system.")

    # 创建缓存目录
    @staticmethod
    def catalogue():
        Cache.__init__system_type()
        word_name = os.path.exists(Cache.__cache_file_path)
        if not word_name:
            os.makedirs(Cache.__cache_file_path)

    @staticmethod
    def get_file_by_app():
        """
        :return: 返回缓存文件路径路径
        """
        Cache.__init__system_type()
        return Cache.__cache_file_path

    @staticmethod
    def get_store_time(name: str) -> str:
        """
        根据缓存文件名获取存储时间
        :param name:
        :return:
        """
        if name in Cache.scan_caches():
            file_time = name.split("-")
            file_time = file_time[-2]+'-'+file_time[-1]
            file_time = file_time.split(".")
            return file_time[0]
        else:
            raise CachedFileDoesNotExist("The {} is does not exist.".format(name))

    @staticmethod
    def get_file_id(name: str) -> str:
        """
        根据根据缓存名获取到文件ID
        :param name:
        :return:
        """
        if name in Cache.scan_caches():
            file_time = name.split("-")
            return file_time[0]

        else:
            raise CachedFileDoesNotExist("The {} is does not exist.".format(name))

    @staticmethod
    def scan_caches() -> tuple:
        """
        跨平台的方式扫描缓存列表
        :param :
        :return:
        """
        Cache.__init__system_type()

        all_cache_file = tuple(os.listdir(Cache.__cache_file_path))

        if len(all_cache_file) == 0:
            return None
        else:
            return all_cache_file

    @staticmethod
    def remove_cache_name(name: str) -> bool:
        """
        删除指定的缓存
        :param name:
        :return:
        """
        # 判断文件存不存在
        if name in Cache.scan_caches():
            os.remove(Cache.__cache_file_path + name)
        else:
            raise CachedFileDoesNotExist("The {} is does not exist.".format(name))

    @staticmethod
    def auto_remove_cache() -> int:
        """
        删除最近30天的缓存文件
        :return:
        """
        Cache.__init__system_type()
        num: int = 0

        all_cache_file = Cache.scan_caches()
        for i in range(len(all_cache_file)):
            filedate = os.path.getatime(Cache.__cache_file_path + all_cache_file[i])
            time1 = datetime.datetime.fromtimestamp(filedate).strftime('%Y-%m-%d')
            date1 = time.time()
            num1 = (date1 - filedate) / 60 / 60 / 24
            if num1 >= 30:
                try:
                    os.remove(Cache.__cache_file_path + all_cache_file[i])
                    #  print(u"已删除文件：%s ： %s" % (time1, all_cache_file[i]))
                    num += 1
                except Exception as e:
                    print(e)

        # if num == 0:
        #     print("No 30 day cache file")
        return num

    @staticmethod
    def remove_all_caches() -> bool:
        """
        删除全部的缓存
        :return:
        """
        Cache.__init__system_type()
        all_cache_file = list(os.listdir(Cache.__cache_file_path))
        for i in range(len(all_cache_file)):
            os.remove(Cache.__cache_file_path + all_cache_file[i])
            # print(u"已删除文件： %s" % (all_cache_file[i]))


if __name__ == '__main__':
 #   Cache.catalogue()
 #   a=Cache.get_store_time('jdk-oracle-17.0.5-20221214-225037.zip')
  #  print(a)

    pass
