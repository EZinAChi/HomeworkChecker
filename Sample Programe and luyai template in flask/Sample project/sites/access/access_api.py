#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : user_api.py
Author       : l-changxuanwei
Create date  : 2022/6/22 3:38 下午 
Description  : 
"""

from flask import request, render_template
from sites.common.base_response import success_response, s_response
from sites.common.errors import ParamErrorException, MethodNotAllowedException, NoFoundRouteException

from sites.access.models import Access


class AccessService(object):
    """
    角色服务
    """

    def list(self):
        """
        列表
        :return:
        """
        if request.method == "GET":
            accesss = Access.objects().all()
            result = []
            for access in accesss:
                result.append({
                    "id": str(access.id),
                    "person_name": str(access.person_name),
                    "time": str(access.time),
                    "type": str(access.type),
                    "note": str(access.note),
                    "temperature": str(access.temperature),
                })
            return s_response(0, result)
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def add(self):
        if request.method == "GET":
            person_name = request.args.get('person_name')
            _time = request.args.get('time')
            _type = request.args.get('type')
            note = request.args.get('note')
            temperature = request.args.get('temperature')
            record = Access()
            record.person_name = person_name
            record.time = _time
            record.type = _type
            record.note = note
            record.temperature = temperature
            record.save()

            return success_response(10000, "success")
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def edit(self):
        if request.method == "GET":
            access_id = request.args.get('id')
            record = Access.objects(id=access_id).first()

            person_name = request.args.get('person_name')
            _time = request.args.get('time')
            _type = request.args.get('type')
            note = request.args.get('note')
            temperature = request.args.get('temperature')
            record.person_name = person_name
            record.time = _time
            record.type = _type
            record.note = note
            record.temperature = temperature
            record.save()

            return success_response(10000, "success")
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def delete(self):
        if request.method == "GET":
            access_id = request.args.get('id')
            Access.objects(id=access_id).delete()

            return success_response(10000, "success")
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def get(self):
        if request.method == "GET":
            access_id = request.args.get('id')
            record = Access.objects(id=access_id).first()

            return success_response(10000, "success",
                                    {"person_name": record.person_name, "id": str(record.id), "time": record.time,"type": record.type,"note": record.note,"temperature": record.temperature})
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def dispatch(self, func):
        """
        函数调度
        """
        map_func = {
            "list": self.list,
            "add": self.add,
            "get": self.get,
            "edit": self.edit,
            "delete": self.delete
        }
        if func in map_func:
            return map_func[func]()
        else:
            raise NoFoundRouteException("URL不存在")
