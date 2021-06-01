import redis
import logging


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
    SESSION_REDIS = redis.StrictRedis(REDIS_HOST, REDIS_PORT)  # 指定session存储位置
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 2  # 设置session的有效期是两天,默认是31天

    # 默认日志等级
    LEVEL = logging.DEBUG


# 开发模式配置信息
class DeveloperConfig(Config):

    pass


# 生产模式配置信息
class ProductConfig(Config):
    DEBUG = False
    LEVEL = logging.ERROR
    pass


# 测试模式配置信息
class TestingConfig(Config):
    TESTING = True


# 设置统一入口管理不同模式
config_dict = {
    'develop': DeveloperConfig,
    'product': ProductConfig,
    'testing': TestingConfig

}

