
from flask import Flask
import sys

# 生成flask对象，传入__name__参数，表示模块名或包名
app = Flask(__name__)

# 定义路由，告诉服务器访问http://127.0.0.1:5000/ hello地址可触发hello()方法
# 类似django中的urls.py文件的功能
@app.route('/hello/')
def hello():
    return 'hello world'


# 直接启动本文件，才执行app.run

if __name__ == '__main__':
    # sys.argv接收启动命令时的参数，如python hello.py 0.0.0.0 80
    ip = sys.argv[1]
    port =sys.argv[2]
    # 参数host代表启动的ip地址，port代表启动的端口
    # debug代表启动的模式
    app.run(host=ip,port=port,debug=True)
    # app.run()