#!/usr/bin/env python3.6
# coding: utf-8
# dao_post.PY
# Created on 2018/1/25
# @author: zhaoyun
"""
description:

"""
from luckynginx import jsonify
from webob import exc
from ..zoo_model.model import session, Post, Dig
import re
from blog.zoo_model.model import Tag,Post_tag

def query_dig_or_bury(post_id):
    dig_query_all = session.query(Dig).filter(Dig.post_id == post_id)
    dig_count = dig_query_all.filter(Dig.state == 1).count()
    dig_list = dig_query_all.filter(Dig.state == 1).order_by(Dig.pubdate.desc()).limit(10).all()
    bury_count = dig_query_all.filter(Dig.state == 0).count()
    bury_list = dig_query_all.filter(Dig.state == 0).order_by(Dig.pubdate.desc()).limit(10).all()
    return [{"count": dig_count, "users": [{"id": x.user_id ,"name":x.post_id} for x in dig_list]},
            {"count": bury_count, "users": [{"id": x.user_id,"name":x.post_id} for x in bury_list]}]

## todo这个方法有点问题： 不能够第二次点或者踩，没有查询state是否存在，操作的时候要注意post_id  different
##500 是正常的，要么成功要么不成功
def dig_or_bury(dig):
    session.add(dig)
    try:
        session.commit()
        return jsonify(message="fuckright")
    except:
        session.rollback()
        return jsonify(status="500")


def pub(post,tags=""):
    taglist = re.split('[\s,]+',tags)
    if taglist != ['']:
        for tag in taglist:
            t = session.query(Tag).filter(Tag.tag==tag).first()
            if t is None:
                t = Tag()
                t.tag= tag
                session.add(t)
            pt = Post_tag()
            pt.tag =t    #t,是实例
            pt.post=post # 实例
            session.add(pt)
    print("dao层", post)
    session.add(post)
    try:
        session.commit()
        return jsonify(post_id=post.id)
    except:
        session.rollback()
        raise exc.HTTPInternalServerError()


def querybypost_id(post_id):
    try:
        return session.query(Post).filter(Post.id == post_id).one()
    except:
        raise exc.HTTPNotFound()

def query_post_tag(post_id):
    try:
        return session.query(Post_tag).filter(Post_tag.post_id == post_id).limit(10).all()
    except:
        raise exc.HTTPNotFound()


def query(author_id,tagname):
    query =session.query(Post)
    if author_id>0:
        query = session.query(Post).filter(Post.author_id ==author_id)
    if tagname!='':
        query.join(Post_tag).join(Tag).filter(Tag.tag==tagname)
    return query

def querybypage(page, size,query):
    try:
        # if author_id>0:
        #     return session.query(Post).filter(Post.author_id ==author_id).order_by(Post.id.desc()).limit(size).offset((page - 1) * size).all()
        return query.order_by(Post.id.desc()).limit(size).offset((page - 1) * size).all()
    except:
        raise exc.HTTPInternalServerError()


def querytotalCount(query):
    try:
        # if author_id>0:
        #     return session.query(Post).filter(Post.author_id ==author_id).count()
        return query.count()
    except:
        return 0
