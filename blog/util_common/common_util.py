#!/usr/bin/env python3.6
# coding: utf-8
#common-util.PY
# Created on 2018/1/23
# @author: zhaoyun
"""
description:

"""
import jwt,datetime
from blog import config

def  gen_token(user_id):
    return jwt.encode({"user_id":user_id,
                       "timestamp":int(datetime.datetime.now().timestamp())},config.AUTH_SECRET,algorithm='HS256').decode()

