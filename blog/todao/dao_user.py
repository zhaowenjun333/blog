#!/usr/bin/env python3.6
# coding: utf-8
#dao_user.PY
# Created on 2018/1/23
# @author: zhaoyun
"""
description:

"""

from luckynginx import jsonify
from webob import exc
from ..zoo_model.model import session, User
from blog.util_common.common_util import gen_token


def querybyemail(email):
    return session.query(User).filter(User.email==email).first()  #duixxiang


def querybyid(id):
    return session.query(User).filter(User.id==id).first()  #duixxiang


def reg(user):
    session.add(user)
    try:
        session.commit()
        return jsonify(token =gen_token(user.id))
    except:
        session.rollback()
        raise exc.HTTPInternalServerError()

    # res = Luckynginx.Response()
    # res.status_code = 200
    # # res.content_type="text/html"
    # print(request)
    # res.text = "<h1>luckynginx</h1>"
    # return res
