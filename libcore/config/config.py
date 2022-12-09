#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from libcore.util.string_util import StringUtil

from libcore.exception.cinfig_key_not_exist_exception import ConfigKeyNnnotExistException


class Config:
    """
    配置
    """
    __allow_config_keys = (
        'mirror',
        'lang',
        'publisher'
    )

    def get(self, key: str) -> str:

        """
        获取配置项
        :param key: key
        :return: Value
        """

        if StringUtil.is_empty(key):
            raise ConfigKeyNnnotExistException("{} is not in config file.because key is empty" .format(key))

        if key not in self.__allow_config_keys:
            raise ConfigKeyNnnotExistException("{} is not in config file.".format(key))

    def set(self, key: str, value: str):
        """
        设置配置项
        :param key: key
        :param value: Value
        :return: 如果不存在这个配置项，那么返回 False
        """
        pass

    def get_with_default(self, key: str, default: str):
        pass


if __name__ == '__main__':
    pass
