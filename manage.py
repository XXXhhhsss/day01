from flask import Flask
from flask_script import Manager

from app.views import blue

app = Flask(__name__)
# 第二步：注册蓝图对象
app.register_blueprint(blueprint=blue,url_prefix='/app')

# @app.route('/hello/')
# def hello():
#     return '还有几天放假'


# 管理flask对象app启动路由
manage = Manager(app)

if __name__ == '__main__':
    # app.run()
    # 启动命令为python manage.py runserver -h 0.0.0.0 -p 80 -d
    # -h 表示Ip端口
    # -p 表示端口
    # -d 表示debug 模式
    manage.run()