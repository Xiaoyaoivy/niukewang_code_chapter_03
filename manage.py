# -*- coding: utf-8 -*-
# 脚本，初始化数据，任务
from nowstagram import app, db
from flask_script import Manager
from sqlalchemy import or_, and_  # 复杂的操作查询
from nowstagram.models import User, Image, Comment
import random

manager = Manager(app)


def get_image_url():
    return 'http://images.nowcoder.com/head' + str(random.randint(0, 1000)) + 'm.png'


@manager.command
def init_database():
    db.drop_all()  # 删除表
    db.create_all()  # 创建表
    for i in range(0, 100):
        db.session.add(User('User' + str(i + 1), 'a' + str(i)))
        for j in range(0, 3):
            db.session.add(Image(get_image_url(), i + 1))
            for k in range(0, 3):
                db.session.add(Comment('This is a comment' + str(k), 1 + 3 * i + j, i + 1))
    db.session.commit()
    # 查询
    print 1, User.query.all()  # 查询所有
    print 2, User.query.get(3)  # 查询第三个用户
    print 3, User.query.filter_by(id=5).first()

    # order_by是排序，desc降序，asc升序 offset偏移（从99开始）,limit（2）只找两个，all打印出所有内容
    # 数据库语句为 select * from user order by id desc limit 1,2
    print 4, User.query.order_by(User.id.desc()).offset(1).limit(2).all()

    print 5, User.query.filter(User.username.endswith('0')).limit(3).all()  # 末尾是0的找出来
    print 6, User.query.filter(or_(User.id == 88, User.id == 99)).all()
    # 没有all语句，可以直接打印sql语句
    print 7, User.query.filter(and_(User.id > 88, User.id < 93)).all()
    print 8, User.query.filter(and_(User.id > 88, User.id < 93)).first_or_404()

    # 分页
    print 9, User.query.paginate(page=1, per_page=10).items
    # 逆序打印print 9, User.query.order_by(User.id.desc()).paginate(page=1, per_page=10).items

    #一对多，打印user关联内容
    user = User.query.get(1)
    print 10, user.images.all()

    image = Image.query.get(1)
    print 11,image.user


if __name__ == '__main__':
    manager.run()
