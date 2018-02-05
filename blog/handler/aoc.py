#!/usr/bin/env python3.6
# coding: utf-8
#aoc.PY
# Created on 2018/1/24
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
from .controller_user import user_router

@user_router.register_preintercepter
def authenticate_pre(ctx, request: Luckynginx.Request):  # 力度太大所以暂时不拦截，放行
    res = service_user.authenticate(ctx, request)
    return res


# 应该提到 aoc里面加强（登录验证功能）某个方法时，装饰到他上面
def authenticate(fn):
    def wrapper(request: Luckynginx.Request):
        try:
            jwtstr = request.headers.get("Jwt")
            print(jwtstr)
            payload = jwt.decode(jwtstr, config.AUTH_SECRET, algorithm='HS256')
            if (datetime.datetime.now().timestamp() - payload.get("timestamp", 0)) > config.AUTH_EXPIRE:
                raise exc.HTTPUnauthorized
            id = payload.get("user_id")
            user = dao_user.querybyid(id)
            if not user:
                raise exc.HTTPUnauthorized
            request.user = user
        except:
            raise exc.HTTPUnauthorized
        return fn(request)  # 提到异常外面就是为了区分是谁出了问题 ,fn有自己的异常机制

    return wrapper
