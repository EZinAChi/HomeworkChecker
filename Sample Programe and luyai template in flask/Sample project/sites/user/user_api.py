#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : user_api.py
Author       : l-changxuanwei
Create date  : 2022/6/22 3:38 下午 
Description  : 
"""

from flask import request
from sites.common.base_response import success_response
from sites.common.errors import ParamErrorException, MethodNotAllowedException, NoFoundRouteException

from sites.user.models import User


class UserService(object):
    """
    用户服务
    """

    def login(self):
        """
        登录
        :return:
        """
        if request.method == "POST":
            user_name = request.json.get('user_name', '')
            pass_word = request.json.get('pass_word', '')
            if not user_name or not pass_word:
                raise ParamErrorException("缺少参数")
            user = User.objects(user_name=user_name, pass_word=pass_word).first()

            if not user:
                raise ParamErrorException("用户名或密码错误")
            return success_response(10000, "success")
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def dispatch(self, func):
        """
        函数调度
        """
        map_func = {
            "login": self.login
        }
        if func in map_func:
            return map_func[func]()
        else:
            raise NoFoundRouteException("URL不存在")
