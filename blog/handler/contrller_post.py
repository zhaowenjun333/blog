#!/usr/bin/env python3.6
# coding: utf-8
#contrller_post.PY
# Created on 2018/1/24
# @author: zhaoyun
"""
description:

"""
from luckynginx.web import Luckynginx
from ..service import service_post
from .aoc import authenticate
post_router = Luckynginx.Router("/post")     ## 这些全部可以分装到配置文件中
Luckynginx.register(post_router)


@post_router.put("^/bury/{id:int}$")
@authenticate
def bury(request: Luckynginx.Request):
    res = service_post.dig_or_bury(request,0)
    return res


@post_router.put("^/dig/{id:int}$")
@authenticate
def dig(request: Luckynginx.Request):
    res = service_post.dig_or_bury(request,1)
    return res


@post_router.post("^/$")
@authenticate
def pub(request: Luckynginx.Request):  # index = idx.get("^/$")(index)   ->index = idx.route(self, rule, *method)(index)
    res = service_post.pub(request)
    return res


@post_router.get("^/{id:int}$")
def get_one_post(request: Luckynginx.Request):  # index = idx.get("^/$")(index)   ->index = idx.route(self, rule, *method)(index)
    res = service_post.get_one_post(request)
    return res


@post_router.get("^/$")
@post_router.get("^/u/{id:int}$")    # 只能单独的查询作者，标签。
@post_router.get("^/t/{tag:str}$")   # 生产中最好用 post，json传参，这样可以任意条件组合。当然，判断会多
def lst(request: Luckynginx.Request):  # index = idx.get("^/$")(index)   ->index = idx.route(self, rule, *method)(index)
    res = service_post.lst(request)
    return res




