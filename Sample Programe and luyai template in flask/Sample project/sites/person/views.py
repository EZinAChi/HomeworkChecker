#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : views.py
Author       : l-changxuanwei
Create date  : 2022/6/22 3:33 下午 
Description  : 
"""
from flask import Blueprint

from sites.person.person_api import PersonService
from sites.common.base_response import exception_handler

person = Blueprint('person', __name__, url_prefix='/person')
person_service = PersonService()


@person.route("<string:func>", methods=['GET', 'POST'])
@exception_handler
def dispatch(func):
    """
    路由调度
    """
    return person_service.dispatch(func)
