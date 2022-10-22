#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : status_code.py
Author       : l-changxuanwei
Create date  : 2022/6/22 3:35 下午 
Description  : 
"""
"""
接口返回状态码定义
key： int类型, 如 10000，共5位
value：string类型，msg信息
"""


STATUS_MSG = {
    10000: "success",

    # 基本系统错误码类别，详细msg可以自己定义
    10001: "用户未登录",
    10002: "参数错误",
    10003: "其它错误",
    10004: "用户无权限",
    10005: "系统错误",

    # 10xxx 映射http_code对应错误
    10404: "Not Found",
    10405: "Method Not Allowed",

    # 11xxxx
    11001: "激活链接已失效",
    11002: "激活链接未失效,已完成修改密码",
    11003: "激活链接未失效,邮箱已经激活"

}
