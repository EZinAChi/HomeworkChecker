#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : mongo_base.py
Author       : l-changxuanwei
Create date  : 2022/6/22 3:25 下午 
Description  : 
"""
from datetime import datetime

from bson import ObjectId
from mongoengine import Document, DateTimeField


class BaseModel(Document):
    # 创建时间
    create_time = DateTimeField(default=datetime.now)
    # 编辑时间
    update_time = DateTimeField(default=datetime.now)

    meta = {'abstract': True, 'strict': False}

    @staticmethod
    def return_fields():
        return ['create_time', 'update_time']


def serialize(data_list, fields='return_fields'):
    results = []
    for data in data_list:
        return_fields = getattr(data, fields)()
        result = dict()
        for field in return_fields:
            value = getattr(data, field)
            if isinstance(value, ObjectId):
                value = str(value)
            if isinstance(value, datetime):
                value = value
            result[field] = value
        results.append(result)
    return results
