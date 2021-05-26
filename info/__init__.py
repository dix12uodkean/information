import redis
from flask import Flask, session
from flask_session import Session  # 指定session存储位置
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import config_dict

# 创建db对象
db = SQLAlchemy()


# 封装函数,工厂模式
def create_app(config_name):

    app = Flask(__name__)

    # 获取配置对象
    config = config_dict[config_name]

    # 加载配置信息到app
    app.config.from_object(config)

    # 初始化app到db中,手动调用
    db.init_app(app)


    # 创建redis的对象
    redis_store = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)

    # 指定session存储位置
    Session(app)

    # 将应用程序使用csrf保护
    CSRFProtect(app)

    return app