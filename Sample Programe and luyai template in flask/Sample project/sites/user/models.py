#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : models.py
Author       : l-changxuanwei
Create date  : 2022/6/22 3:23 下午 
Description  : 
"""
from sites.common.mongo_base import BaseModel

from mongoengine import StringField


class User(BaseModel):
    """
    用户表
    """
    # 用户名
    user_name = StringField(default='')
    # 密码
    pass_word = StringField(default='')

    meta = {"collection": "user",
            "index_background": True,
            "indexes": []}

    @staticmethod
    def return_fields():
        return ["id", 'user_name', 'pass_word']

