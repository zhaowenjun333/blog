#!/usr/bin/env python3.6
# coding: utf-8
#config.py.PY
# Created on 2018/1/22
# @author: zhaoyun
"""
description:

"""
USERNAME="root"
PASSWD="123456"
# IP="172.16.101.67"   #192.168.8.130
IP="192.168.8.130"   #192.168.8.130   和vmip有关192.168.8.1
PORT=3306
DBNAME="blog"
PARAMS ="charset=utf8"
URL="mysql+pymysql://{}:{}@{}:{}/{}?{}".format(USERNAME,PASSWD,
                                               IP,PORT,DBNAME,PARAMS)
DATABASE_DEBUG=True
WSIP = "0.0.0.0"
WSPORT = 8000

AUTH_SECRET ="beijing"
AUTH_EXPIRE = 8*60*60
