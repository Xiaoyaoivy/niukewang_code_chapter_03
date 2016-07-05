# -*- coding: utf-8 -*-
from nowstagram import db
from datetime import datetime  # 导入时间用于class Image
import random


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id是数据库中的一列，主键，自增长
    content = db.Column(db.String(1024))  # 内容
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))  # 外键
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键
    status = db.Column(db.Integer, default=0)  # 0正常，1表示被删除
    user = db.relationship('User')

    def __init__(self, content, image_id, user_id):
        self.content = content
        self.image_id = image_id
        self.user_id = user_id

    def __repr__(self):
        return '<Comment %d %s>' % (self.id, self.content)


"""图片地址为：http://images.nowcoder.com/head/99m.png"""


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id是数据库中的一列，主键，自增长
    url = db.Column(db.String(512))  # 地址
    # foreignkey表示图片的user_id从User中的user.id来
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_date = db.Column(db.DATETIME)
    comments = db.relationship('Comment')

    def __init__(self, url, user_id):
        self.url = url
        self.user_id = user_id
        self.created_date = datetime.now()

    def __repr__(self):
        return '<Image %d %s>' % (self.id, self.url)


class User(db.Model):
    # __tablename__ = 'xuser' 增加这句，需要把之前上面关联的ForeignKey和user有关的都改成xuser
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id是数据库中的一列，主键，自增长
    username = db.Column(db.String(80), unique=True)  # 定义为字符串类型，unique保证唯一
    password = db.Column(db.String(32))  # 定义为字符串类型
    head_url = db.Column(db.String(256))  # 头像
    #images = db.relationship('Image')  # 关联表

    """
    image = Image.query.get(1)
    print 11,image.user

    增加backref = user,内置一个变量
    """
    images = db.relationship('Image',backref = 'user',lazy = 'dynamic')#关联属性


    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.head_url = 'http://images.nowcoder.com/head' + str(random.randint(0, 1000)) + 'm.png'  # 使用牛客网自带的1000张随机图片

    def __repr__(self):
        return '<User %d %s>' % (self.id, self.username)
