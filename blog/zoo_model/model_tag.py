#!/usr/bin/env python3.6
# coding: utf-8
# model_tag.PY
# Created on 2018/2/1
# @author: zhaoyun
"""
description:

"""

from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, DateTime, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import relationship


from sqlalchemy import Column, BigInteger,String,ForeignKey
from sqlalchemy.orm import  relationship
from sqlalchemy import create_engine
from blog import config
from sqlalchemy.ext.declarative import declarative_base
Base =declarative_base()



engine = create_engine(config.URL, echo=config.DATABASE_DEBUG)


def createtables():
    Base.metadata.create_all(engine)

def droptables():
    Base.metadata.drop_all(engine)


# if __name__ == "__main__":
#     # from .model import Post
#     droptables()
#     createtables()
