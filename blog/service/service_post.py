#!/usr/bin/env python3.6
# coding: utf-8
# service_post.PY
# Created on 2018/1/24
# @author: zhaoyun
"""
description:

"""
from blog.zoo_model.model import Post, Content
from luckynginx import jsonify
from ..todao import dao_post
import datetime, math                         #导入叫做 名词空间  不管是方法 还是变量
from blog.zoo_model.model import Dig


def dig_or_bury(request,value=1):
    user_id = request.user.id
    post_id =request.kwargs.id
    dig=Dig()
    dig.user_id=user_id
    dig.post_id=post_id
    dig.state=value
    dig.pubdate=datetime.datetime.now()
    return dao_post.dig_or_bury(dig)


def pub(request):
    print(request.json)
    payload = request.json
    post = Post()
    try:
        post.title = payload["title"]
        post.author_id = request.user.id
        post.postdate = datetime.datetime.now()
        content = Content()
        content.content = payload["content"]
        post.content = content  # 截取前 十个字?可以，不是这种设计
        tags = payload['tags']
    except Exception as e:
        print("service pub down")
    return dao_post.pub(post,tags)


def get_one_post(request):
    print(request.kwargs.id)
    post_id = request.kwargs.id
    post = dao_post.querybypost_id(post_id)
    post.hits += 1
    _ = dao_post.pub(post)
    print(">>>>", post.postdate)
    #赞踩
    user = post.author
    dig_info,bury_info=dao_post.query_dig_or_bury(post_id)
    #处理tag
    pts=dao_post.query_post_tag(post_id)
    tags = "".join([x.tag.tag for x in pts])
    return jsonify(post={"post_id": post.id,  # 特别注意能被json化的只有基本类型，引用类型的只有两个可以元祖和列表
                         "author": user.name,
                         "author_id": post.author_id,
                         "title": post.title,
                         "postdate": post.postdate.timestamp()},
                   dig_info=dig_info,
                   bury_info=bury_info,
                   tags = tags
                   )


def lst(request):
    print(request.kwargs)
    try:
        page = int(request.params.get("page", 1))
        page = page if page > 0 else 1
    except:
        page = 1
    try:
        size = int(request.params.get("size", 4))
        size = size if (size > 0) and size < 101 else 20
    except :
        size = 20
    try: ##作者id
        author_id = int(request.kwargs.id)
        author_id = author_id if (author_id > 0) else -1
    except :
        author_id = -1
    try: ##标签名称
        tagname = str(request.kwargs.tag)
        tagname = tagname if (len(tagname) > 0) else ""
    except :
        tagname = ""
    query = dao_post.query(author_id,tagname)   # 把过滤条件一次性查询出来不必要后面每个都做一次
    count = dao_post.querytotalCount(query)
    posts = dao_post.querybypage(page, size,query )
    return jsonify(posts=[{
        "post_id": post.id,
        "title": post.title,
    } for post in posts],
        page_info={
            "page": page,
            "size": size,
            "count": count,
            "pages": math.ceil(count / size)
        })
