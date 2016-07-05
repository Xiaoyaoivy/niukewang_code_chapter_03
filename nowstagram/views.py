# -*- coding: utf-8 -*-
# 视图
from nowstagram import app


@app.route('/')
def index():
    return 'Hello'
