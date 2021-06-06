from flask import current_app
from . import index_blue
from info import redis_store


@index_blue.route('/', methods=['GET', 'POST'])
def index():

    # # 测试redis是否可以跑通
    redis_store.set('name', 'zhangsan')

    name = redis_store.get('name')

    print(name)

    # session['name'] = 'banzhang'

    # current_app.debug('调试信息aaaaa')
    # current_app.error('错误信息aaaaa')

    return 'hello'
