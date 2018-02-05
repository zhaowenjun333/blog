#!/usr/bin/env python3.6
# coding: utf-8
#service_user.PY
# Created on 2018/1/23
# @author: zhaoyun
"""
description:

"""
from blog.util_common.common_util import  gen_token
import bcrypt
from ..zoo_model.model import User
from webob import exc
from ..todao import dao_user
from luckynginx import jsonify


def authenticate(ctx,request):
    try:
        print(">"*10,request.json,"<"*10)  #拦截器沦落为打印
        # jwtstr = request.headers.get("Jwt")
        # print(jwtstr)
        # payload = jwt.decode(jwtstr,config.AUTH_SECRET,algorithm='HS256')
        # if(datetime.datetime.now().timestamp()-payload.get("timestamp",0)) > config.AUTH_EXPIRE:
        #     raise exc.HTTPUnauthorized
        # id = payload.get("id")
        # if not dao_user.querybyid(id):
        #     raise exc.HTTPUnauthorized
        return request
    except Exception as e :
        raise e()


def login(request):
    payload = request.json
    email = payload.get("email")
    user =dao_user.querybyemail(email)
    if user and bcrypt.checkpw(payload.get("password").encode(),user.password.encode()):
        return jsonify(user={"id":user.id,"name":user.name,
                             "email":user.email},token =gen_token(user.id))
    else:
        raise exc.HTTPUnauthorized()


def reg(request):
    payload  =request.json
    email = payload.get("email")
    if dao_user.querybyemail(email) is not None:
        raise exc.HTTPConflict("{} is already exists".format( email))
    user =User()
    payload  =request.json
    try:
        user.name=payload.get("name")
        user.email=payload["email"]
        user.password=bcrypt.hashpw(payload["password"].encode(),
                                    bcrypt.gensalt())
    except:
        raise exc.HTTPBadRequest()
    return dao_user.reg(user)

