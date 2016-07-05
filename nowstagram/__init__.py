# -*- coding: utf-8 -*-
# 导出
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_pyfile('app.conf')  # app初始化
db = SQLAlchemy(app)  # 操作数据库

from nowstagram import views, models
