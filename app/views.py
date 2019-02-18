
from flask import Blueprint,\
    redirect,url_for,abort,render_template,request,make_response





# 第一步，初始化蓝图对象，斌使用对象管理路由
# 初始化蓝图对象，蓝图用于模块化管理路由
blue = Blueprint('first',__name__)

# 蓝图对象.route(路由)
@blue.route('/hello/')
def hello():
    return '还有几天放假'


# 路由规则
# <int:id>  表示接收的id值为int类型
# <string:name> 表示接收的name 参数为string类型
# <float:num> 浮点数
# <uuid：uid> 表示接收的uid参数为uuid类型值
# <path:path> 表示接收的p变量为路径


@blue.route('/stu/<int:id>/')
def stu(id):
    return 'hello stu id:%s' % id

@blue.route('/name/<string:name>/')
def stu_name(name):
    return 'hello stu: %s' % name


@blue.route('/float/<float:num>/')
def float_num(num):
    return 'float num: %.2f' % num

@blue.route('/get_uuid/')
def get_uuid():
    import uuid
    return 'uuid: %s' % str(uuid.uuid4())

@blue.route('/uuid/<uuid:uid>/')
def uuid(uid):
    return 'uid: %s' % uid

@blue.route('/path/<path:p>/')
def get_path(p):
    return 'path:%s' % p

@blue.route('/redirect_hello/')
def redirect_hello():
    # 实现直接重定向
    # 第一种方式
    # return redirect('/app/hello/')
    # 第二种方式：使用url_for的形式进行反向解析
    # url_for（‘生成蓝图的第一个参数，重定向的函数名’）
    # 无参数的跳转
    # return redirect(url_for('first.hello'))
    # 有参的跳转
    return redirect(url_for('first.stu', id=1))


# 抛出错误 abort
@blue.route('/index/')
def index():
    try:
        a = 1
        b = 0
        c = a/b
    except Exception as e:
        abort(500)
    return 'hello'

# 捕获500错误，处理错误
@blue.errorhandler(500)
def error_500(e):
    return 'exception : %s' % e

@blue.route('/my_index/',methods=['GET','POST','PUT','DELETE'])
def my_index():
    if request.method == 'GET':
    # 模板index.html存在templates文件夹下，
    # 且templates文件夹和manage.py文件同级

    # 接收参数,使用request.args取值
    # request.args.get(key) 或者request.args.getlist（key）
        return render_template('index.html')
    if request.method == 'POST':
        # 接收参数
        # 使用request.form取值
        # request.form.get(key) 或者request.form.getlist（key）
        pass

@blue.route('/response/',methods=['GET'])
def get_response():
    # 响应字符串
    # res = make_response('<h3>放假啦</h3>', 200)

    # 响应模板文件
    html = render_template('index.html')
    res = make_response(html,200)
    # token的生成
    res.set_cookie('token','48555252',max_age=10)
    # 删除token,跟django的写法一样
    # res.delete_cookie('token')
    return res