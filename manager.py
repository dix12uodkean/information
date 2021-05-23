import redis
from flask import Flask, session
from flask_session import Session  # 指定session存储位置
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
app = Flask(__name__)


# 配置信息
class Config(object):

    SECRET_KEY = 'sdnwncencnec'
    DEBUG = True

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pymsql@192.168.104.116:3306/information'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis的配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 配置 session信息
    SESSION_TYPE = 'redis'  # 指定session存储类型
    SESSION_USE_SIGNER = True  # 设置session签名
    SESSION_REDIS = redis.StrictRedis(REDIS_HOST,REDIS_PORT)  # 指定session存储位置
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 2  # 设置session的有效期是两天,默认是31天


# 加载配置信息到app
app.config.from_object(Config)


# 创建db对象
db = SQLAlchemy(app)

# 创建redis的对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 指定session存储位置
Session(app)

# 将应用程序使用csrf保护
CSRFProtect(app)

# 配置数据库迁移
manager = Manager(app)
Migrate(app, db)
manager.add_command('db',MigrateCommand)


@app.route('/', methods=['GET', 'POST'])
def index():

    # # 测试redis是否可以跑通
    # redis_store.set('name', 'zhangsan')
    #
    # name = redis_store.get('name')
    #
    # print(name)

    session['name'] = 'banzhang'
    return 'hello'


if __name__ == '__main__':
    manager.run()