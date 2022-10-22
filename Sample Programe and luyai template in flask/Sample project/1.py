#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : 1.py
Author       : l-changxuanwei
Create date  : 2022/9/17 3:38 下午 
Description  : 
"""
from sites.user.models import User
record=User()
record.pass_word='admin123'
record.user_name='admin'
record.save()