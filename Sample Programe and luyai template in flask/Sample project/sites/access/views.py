#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : views.py
Author       : l-changxuanwei
Create date  : 2022/6/22 3:33 下午 
Description  : 
"""
from flask import Blueprint

from sites.access.access_api import AccessService
from sites.common.base_response import exception_handler

access = Blueprint('access', __name__, url_prefix='/access')
access_service = AccessService()


@access.route("<string:func>", methods=['GET', 'POST'])
@exception_handler
def dispatch(func):
    """
    路由调度
    """
    return access_service.dispatch(func)
