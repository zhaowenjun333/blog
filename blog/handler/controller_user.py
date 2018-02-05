#!/usr/bin/env python3.6
# coding: utf-8
# user.PY
# Created on 2018/1/23
# @author: zhaoyun
"""
description:

"""
from blog import config
from blog.todao import dao_user
import datetime, jwt
from webob import exc
from luckynginx.web import Luckynginx
from ..service import service_user

user_router = Luckynginx.Router("/user")  ## 这些全部可以分装到配置文件中
Luckynginx.register(user_router)


@user_router.post("^/reg$")
def reg(request: Luckynginx.Request):  # index = idx.get("^/$")(index)   ->index = idx.route(self, rule, *method)(index)
    res = service_user.reg(request)
    return res


@user_router.post("^/login$")
def login(request: Luckynginx.Request):
    res = service_user.login(request)
    return res




