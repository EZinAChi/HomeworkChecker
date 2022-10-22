#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : views.py
Author       : l-changxuanwei
Create date  : 2022/6/22 3:33 下午 
Description  : 
"""
from flask import Blueprint

from sites.user.user_api import UserService
from sites.common.base_response import exception_handler

user = Blueprint('user', __name__, url_prefix='/user')
user_service = UserService()


@user.route("<string:func>", methods=['GET', 'POST'])
@exception_handler
def dispatch(func):
    """
    路由调度
    """
    return user_service.dispatch(func)
