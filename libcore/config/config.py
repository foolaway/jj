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

        if StringUtil.is_empty(key):
            raise ConfigKeyNnnotExistException()

        if key not in self.__allow_config_keys:
            raise ConfigKeyNnnotExistException()

    def set(self, key: str, value: str):
        pass

    def get_with_default(self, key: str, default: str):
        pass


if __name__ == '__main__':
    pass
