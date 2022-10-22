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


class Access(BaseModel):
    """
    出入管理
    """
    # 人员名称
    person_name = StringField(default='')
    # 时间
    time = StringField(default='')
    type = StringField(default='')
    note = StringField(default='')
    temperature = StringField(default='')

    meta = {"collection": "access",
            "index_background": True,
            "indexes": []}

    @staticmethod
    def return_fields():
        return ["id", 'person_name', 'age']
