#!/usr/bin/env python3.6
# coding: utf-8
#model.PY
# Created on 2018/1/22
# @author: zhaoyun
"""
description:

"""
from sqlalchemy import Column,Integer,BigInteger,String,ForeignKey,DateTime,PrimaryKeyConstraint,UniqueConstraint
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import LONGTEXT
from blog import config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import TINYINT
Base =declarative_base()


class User(Base):
    __tablename__="user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(48),nullable=False)
    email = Column(String(64),nullable=False,unique=True)
    password =Column(String(128),nullable=False )

    def __repr__(self):
        return "<User(id={},name={},email={},password={})>".format(
            self.id,self.name,self.email,self.password
        )


class Post(Base):
    __tablename__="post"
    id = Column(BigInteger,primary_key=True,autoincrement=True)
    title=Column(String(256),nullable=False)
    author_id=Column(Integer,ForeignKey("user.id"),nullable=False)
    postdate = Column(DateTime,nullable=False)
    author = relationship("User")
    content = relationship("Content",uselist =False)
    hits =Column(BigInteger,nullable=False,default=0,index=True)

    def __repr__(self):
        return "<Post(id={},postdate={},title={},author_id={})>".format(
            self.id,self.postdate,self.title,self.author_id
        )


class Content(Base):
    __tablename__ ="content"
    id =Column(BigInteger,ForeignKey("post.id"),primary_key=True)
    content=Column(LONGTEXT,nullable=False)
    def __repr__(self):
        return "<Content(id={},content={} )>".format(
            self.id,self.content
        )


class Dig(Base):
    __tablename__ = "dig"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)
    post_id = Column(BigInteger, ForeignKey("post.id"), nullable=False, index=True)
    state = Column(TINYINT, nullable=False)
    pubdate = Column(DateTime, nullable=False)
    __table_args__ = (UniqueConstraint("user_id", "post_id", name="unq_user_post"),)

    def __repr__(self):
        return "<Dig(id={},user_id={},post_id={},state={})>".format(self.id, self.user_id, self.post_id, self.state)

class Tag(Base):
    __tablename__ = "tag"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    tag = Column(String(16), nullable=False, unique=True)


class Post_tag(Base):
    __tablename__ = "post_tag"
    post_id = Column(BigInteger, ForeignKey("post.id"), nullable=False)
    tag_id = Column(BigInteger, ForeignKey("tag.id"), nullable=False)
    __table_args__ = (PrimaryKeyConstraint("post_id", "tag_id"),)
    post = relationship("Post")
    tag = relationship("Tag")



engine = create_engine(config.URL, echo=config.DATABASE_DEBUG)


def createtables():
    Base.metadata.create_all(engine)

def droptables():
    Base.metadata.drop_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

