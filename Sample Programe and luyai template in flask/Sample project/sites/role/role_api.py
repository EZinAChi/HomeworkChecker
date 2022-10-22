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

from sites.role.models import Role


class RoleService(object):
    """
    角色服务
    """

    def list(self):
        """
        列表
        :return:
        """
        if request.method == "GET":
            roles = Role.objects().all()
            result = []
            for role in roles:
                result.append({
                    "id": str(role.id),
                    "role_name": str(role.role_name),
                    "note": str(role.note),
                })
            return s_response(0, result)
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def add(self):
        if request.method == "GET":
            role_name = request.args.get('role_name')
            note = request.args.get('note')
            record = Role()
            record.role_name = role_name
            record.note = note
            record.save()

            return success_response(10000, "success")
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def edit(self):
        if request.method == "GET":
            role_name = request.args.get('role_name')
            note = request.args.get('note')
            role_id = request.args.get('id')
            record = Role.objects(id=role_id).first()
            record.role_name = role_name
            record.note = note
            record.save()

            return success_response(10000, "success")
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def delete(self):
        if request.method == "GET":
            role_id = request.args.get('id')
            Role.objects(id=role_id).delete()

            return success_response(10000, "success")
        else:
            raise MethodNotAllowedException("GET Method Not Allowed")

    def get(self):
        if request.method == "GET":
            role_id = request.args.get('id')
            record = Role.objects(id=role_id).first()

            return success_response(10000, "success",
                                    {"role_name": record.role_name, "id": str(record.id), "note": record.note})
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
            "delete":self.delete
        }
        if func in map_func:
            return map_func[func]()
        else:
            raise NoFoundRouteException("URL不存在")
