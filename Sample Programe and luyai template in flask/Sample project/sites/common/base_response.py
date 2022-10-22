#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : base_response.py
Author       : l-changxuanwei
Create date  : 2022/6/22 3:34 下午 
Description  : 
"""
import csv
import sys
import traceback
import logging
from io import StringIO

from flask import make_response, request, stream_with_context, Response
from functools import wraps

from sites.common.status_code import STATUS_MSG
from sites.common.json_utils import json_encode
from sites.common.errors import ParamErrorException, INFO_EXCEPTION_LIST


def get_argument(arg_name, arg_cast, arg_default):
    """
    获取参数
    :param arg_name:
    :param arg_cast:
    :param arg_default:
    :return:
    """
    value = request.values.get(arg_name)
    if not value:
        if arg_default is None:
            raise ParamErrorException("param %s is missing" % arg_name)
        else:
            return arg_default
    if arg_cast:
        try:
            value = arg_cast(value)
        except Exception:
            raise ParamErrorException("param %s type mismatch" % arg_name)
    return value


# 异常处理
def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except INFO_EXCEPTION_LIST as e:
            return success_response(e.status_code, str(e), http_code=e.http_code)
        except Exception as e:
            exc_type, exc_value, exc_traceback_obj = sys.exc_info()
            traceback.print_tb(exc_traceback_obj)
            logging.error(e)
            return success_response(10005, "server wrong", http_code=200)

    return wrapper


def success_response(status, msg=None, info=None, http_code=200, total_count=0):
    if not msg:
        msg = STATUS_MSG.get(status, '')
    data = {'status': status, 'msg': msg}
    if info is not None:
        data['data'] = info
    if total_count:
        data['total_count'] = total_count
    return make_response((
        json_encode(data),
        http_code,
        {'Content-Type': 'application/json; charset=utf-8'}
    ))


def s_response(status, data=None, http_code=200):
    data = {'code': status, 'data': data}
    return make_response((
        json_encode(data),
        http_code,
        {'Content-Type': 'application/json; charset=utf-8'}
    ))


def success_response_csv_log(status, msg=None, info=None, http_code=200, total_count=0):
    if not msg:
        msg = STATUS_MSG.get(status, '')
    data = {'status': status, 'msg': msg}
    if total_count:
        data['total_count'] = total_count

    def generate():
        io = StringIO()
        w = csv.writer(io)
        # writer
        for i in info:
            w.writerow(i)
            yield io.getvalue()
            io.seek(0)
            io.truncate(0)

    response = Response(stream_with_context(generate()), mimetype='text/csv')
    response.headers.set("Content-Disposition", "attachment", filename="auditlog.csv")
    response.headers['data'] = data
    return response


def base_response(data, http_code=200):
    """
    原始返回
    """
    return make_response((
        json_encode(data),
        http_code,
        {'Content-Type': 'application/json; charset=utf-8'}
    ))
