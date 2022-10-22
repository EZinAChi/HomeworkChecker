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

from sites.person.models import Person


class PersonService(object):
    """
    角色服务
    """

    def list(self):
        """
        列表
        :return:
        """
        if request.method == "GET":
            persons = Person.objects().all()
            result = []
            for person in persons:
                result.append({
                    "id": str(person.id),
                    "role_name": str(person.role_name),
                    "age": str(person.age),
                    "sex": str(person.sex),
                    "name": str(person.name),
                })
            return s_response(0, result)
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def add(self):
        if request.method == "GET":
            role_name = request.args.get('role_name')
            age = request.args.get('age')
            sex = request.args.get('sex')
            name = request.args.get('name')
            record = Person()
            record.role_name = role_name
            record.age = age
            record.sex = sex
            record.name = name
            record.save()

            return success_response(10000, "success")
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def edit(self):
        if request.method == "GET":
            person_id = request.args.get('id')

            role_name = request.args.get('role_name')
            age = request.args.get('age')
            sex = request.args.get('sex')
            name = request.args.get('name')
            record = Person.objects(id=person_id).first()
            record.role_name = role_name
            record.age = age
            record.sex = sex
            record.name = name
            record.save()

            return success_response(10000, "success")
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def delete(self):
        if request.method == "GET":
            person_id = request.args.get('id')
            Person.objects(id=person_id).delete()

            return success_response(10000, "success")
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def get(self):
        if request.method == "GET":
            person_id = request.args.get('id')
            record = Person.objects(id=person_id).first()

            return success_response(10000, "success",
                                    {"role_name": record.role_name, "id": str(record.id), "age": record.age,"sex": record.sex,"name": record.name})
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
