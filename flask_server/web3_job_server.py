import random
import time
from flask import Flask, request, json

from flask_server.utils import web3_career_redis

# 实例化一个web服务对象
app = Flask(__name__)


# 创建一个方法来处理请求
# 定义一个路由，访问服务的根目录就可以得到结果
@app.route('/')
def hello():
    return '<h1>hello flask</h1>'


# 构造一个接受post请求的响应
@app.route('/post', methods=['POST'])
def test_post():
    # 处理接口发送过来的两个参数，将两个参数合并成一个字符串返回
    d1 = request.form['d1']
    d2 = request.form['d2']
    return d1 + d2


# 处理极简交易接口
@app.route('/job/web3.career', methods=['POST'])
def web3_career_job_list():
    # 拿到客户端返回的数据
    res = json.loads(request.get_data())
    data = web3_career_redis.get_web3_career_jobs_all()

    # 把out_trade_no改成客户端发送过来的数据

    # 验证授权码
    # if auth_code != '28763443825664394':
    #     return {'coode': '50000', 'msg': '请求码验证失败'}

    return data


if __name__ == '__main__':
    # 运行服务，并确定服务运行的IP和端口
    app.run('127.0.0.1', '1235')
