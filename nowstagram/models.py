# -*- coding: utf-8 -*-
from nowstagram import db
from datetime import datetime #导入时间用于class Image
import random

"""图片地址为：http://images.nowcoder.com/head/99m.png"""
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id是数据库中的一列，主键，自增长
    url = db.Column(db.String(512))#地址
    # foreignkey表示图片的user_id从User中的user.id来
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    created_date = db.Column(db.DATETIME)

    def __init__(self,url,user_id):
        self.url = url
        self.user_id = user_id
        self.created_date = datetime.now()

    def __repr__(self):
        return '<Image %d %s>' % (self.id, self.url)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id是数据库中的一列，主键，自增长
    username = db.Column(db.String(80), unique=True)  # 定义为字符串类型，unique保证唯一
    password = db.Column(db.String(32))  # 定义为字符串类型
    head_url = db.Column(db.String(256))  # 头像
    images = db.relationship('Image') #关联表

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.head_url = 'http://images.nowcoder.com/head' + str(random.randint(0, 1000)) + 'm.png'  # 使用牛客网自带的1000张随机图片

    def __repr__(self):
        return '<User %d %s>' % (self.id, self.username)
