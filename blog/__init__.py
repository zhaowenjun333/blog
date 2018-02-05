#!/usr/bin/env python3.6
# coding: utf-8
#__init__.py.PY
# Created on 2018/1/23
# @author: zhaoyun
"""
description:

"""
from wsgiref.simple_server import make_server
from luckynginx.web import Luckynginx
from blog.config import *
from blog.handler import controller_user
from blog.handler import contrller_post
if __name__ == "__main__":
    httpd = make_server( WSIP,  WSPORT, Luckynginx())
    try:
        print("service  starting")
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
        httpd.server_close()


