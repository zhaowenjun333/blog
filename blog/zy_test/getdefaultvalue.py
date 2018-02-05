#!/usr/bin/env python3.6
# coding: utf-8
#getdefaultvalue.PY
# Created on 2018/1/24
# @author: zhaoyun
"""
description:

"""
def getDefault(k,value):
    # inputvalue= int(request.params.get(value,1))
    if value =="page":
        try:
            inputvalue= int(k.get(value,1))
            if value =="page":
                if inputvalue <1:
                    inputvalue=1
            else:
                if inputvalue <1 or inputvalue>100:
                    pass
        except:
            if value =="page":
                inputvalue=1
            else:
                inputvalue=1
    return  inputvalue
