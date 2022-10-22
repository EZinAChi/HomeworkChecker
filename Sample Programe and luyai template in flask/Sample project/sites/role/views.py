#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : views.py
Author       : l-changxuanwei
Create date  : 2022/6/22 3:33 下午 
Description  : 
"""
from flask import Blueprint

from sites.role.role_api import RoleService
from sites.common.base_response import exception_handler

role = Blueprint('role', __name__, url_prefix='/role')
role_service = RoleService()


@role.route("<string:func>", methods=['GET', 'POST'])
@exception_handler
def dispatch(func):
    """
    路由调度
    """
    return role_service.dispatch(func)
