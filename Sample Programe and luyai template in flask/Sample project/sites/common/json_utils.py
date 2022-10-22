#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : json_utils.py
Author       : l-changxuanwei
Create date  : 2022/6/22 3:35 下午 
Description  : 
"""

import json

_j_modules = [
    ('ujson', 'dumps', TypeError, 'loads', ValueError),
    ('yajl', 'dumps', TypeError, 'loads', ValueError),
    ('jsonlib2', 'write', 'WriteError', 'read', 'ReadError'),
    ('jsonlib', 'write', 'WriteError', 'read', 'ReadError'),
    ('cjson', 'encode', 'EncodeError', 'decode', 'DecodeError'),
    ('simplejson', 'dumps', TypeError, 'loads', ValueError),
    ('json', 'dumps', TypeError, 'loads', ValueError),
]
_j_fields = ('modname', 'encoder', 'encerror', 'decoder', 'decerror')

JSON_ENCODER_ERR_MESSAGE = '''Json Encoder Error :
      > Error : %s
      > Value : %s'''

JSON_DECODER_ERR_MESSAGE = '''Json Decoder Error :
      > Error : %s
      > Value : %s'''


class JsonImplementation(object):
    def __init__(self, module_desc):
        self._module_desc = dict(zip(_j_fields, module_desc))
        self._json = self._load_module()

        self._j_encoder = None
        self._j_decoder = None
        self._j_enc_err = None
        self._j_dec_err = None

        self._load_module_function()

    def _load_module(self):
        module_name = self._module_desc['modname']
        return __import__(module_name)

    def _load_module_function(self):
        self._j_encoder = getattr(self._json, self._module_desc['encoder'])
        self._j_decoder = getattr(self._json, self._module_desc['decoder'])

        self._j_enc_err = self._module_desc['encerror']
        self._j_dec_err = self._module_desc['decerror']

        if isinstance(self._j_enc_err, str):
            self._j_enc_err = getattr(self._json, self._j_enc_err)

        if isinstance(self._j_dec_err, str):
            self._j_dec_err = getattr(self._json, self._j_dec_err)

    def json_encode(self, obj):
        try:
            return self._j_encoder(obj)
        except self._j_enc_err as e:
            raise TypeError(JSON_ENCODER_ERR_MESSAGE % (e, obj))

    def json_decode(self, obj):
        try:
            return self._j_decoder(obj)
        except self._j_dec_err as e:
            raise ValueError(JSON_DECODER_ERR_MESSAGE % (e, obj))


for module_desc in _j_modules:
    try:
        json_imp = JsonImplementation(module_desc)
        break
    except ImportError:
        pass
else:
    raise ImportError("No supported JSON module found")


def json_encode(value):
    return json_imp.json_encode(value)


def json_decode(value):
    return json_imp.json_decode(value)


def json_name():
    return json_imp._module_desc['modname']


def json_view(value):
    if isinstance(value, basestring):
        try:
            value = json_decode(value)
        except ValueError:
            pass
    return json.dumps(value, indent=2)


def select_json(json_module_name):
    global json_imp

    for j_desc in _j_modules:
        if j_desc[0] == json_module_name:
            json_imp = JsonImplementation(j_desc)
            return

    raise ImportError('No module named : %s' % (json_module_name))
