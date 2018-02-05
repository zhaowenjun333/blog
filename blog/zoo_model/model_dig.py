#!/usr/bin/env python3.6
# coding: utf-8
# model.PY
# Created on 2018/1/22
# @author: zhaoyun
"""
description:

"""
from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import LONGTEXT
from blog import config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import TINYINT
Base = declarative_base()



class Subject(Base):
    __tablename__ ="subject"
    id =Column(Integer,primary_key=True)
    subjectname=Column(String(64),nullable=False)


class Course(Base):
    __tablename__ ="course"
    id =Column(Integer,ForeignKey("subject.id"),primary_key=True)
    coursename=Column(String(64),nullable=False)


engine = create_engine(config.URL, echo=config.DATABASE_DEBUG)


def createtables():
    Base.metadata.create_all(engine)


def droptables():
    Base.metadata.drop_all(engine)


# if __name__ == "__main__":
#     # from .model import Post
#     droptables()
#     createtables()
