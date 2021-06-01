import logging
from logging.handlers import RotatingFileHandler
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

    # 调用方法,集成日志文件
    log_file(config.LEVEL)

    # 初始化app到db中,手动调用
    db.init_app(app)

    # 创建redis的对象
    redis_store = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)

    # 指定session存储位置
    Session(app)

    # 将应用程序使用csrf保护
    CSRFProtect(app)

    return app


# 集成日志文件,作用:用来记录程序的运行过程,方便运维人员查看
def log_file(level):

    # 设置日志的记录等级
    logging.basicConfig(level=level)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/logs", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


