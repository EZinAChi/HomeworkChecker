#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : errors.py
Author       : l-changxuanwei
Create date  : 2022/6/22 3:37 下午 
Description  : 
"""


class ParamErrorException(Exception):
    """
    参数错误
    """

    def __init__(self, message):
        self.msg = message
        self.status_code = 10002
        self.http_code = 200


class MethodNotAllowedException(Exception):
    """
    请求方法不允许
    """

    def __init__(self, message):
        self.msg = message
        self.status_code = 10405
        self.http_code = 405


class NoFoundRouteException(Exception):
    """
    未找到路由
    """

    def __init__(self, message):
        self.msg = message
        self.status_code = 10404
        self.http_code = 404

INFO_EXCEPTION_LIST = (NoFoundRouteException, \
                       MethodNotAllowedException, ParamErrorException)