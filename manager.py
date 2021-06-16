
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from info import create_app, db, models
# 调用方法获取app对象
app = create_app('develop')  # -->从'config_dict'里获取

# 配置数据库迁移
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()