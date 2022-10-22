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


class Person(BaseModel):
    """
    人员
    """
    # 角色名称
    role_name = StringField(default='')
    # 年龄
    age = StringField(default='')
    sex = StringField(default='')
    name = StringField(default='')

    meta = {"collection": "person",
            "index_background": True,
            "indexes": []}

    @staticmethod
    def return_fields():
        return ["id", 'role_name', 'age']

