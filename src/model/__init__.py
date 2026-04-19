from flask_sqlalchemy import SQLAlchemy

from src.config.env import switch

# 虚拟数据库对象，用于在数据库连接失败时使用
class DummyDB:
    def Column(self, *args, **kwargs):
        return None
    
    def String(self, *args, **kwargs):
        return None
    
    def Integer(self, *args, **kwargs):
        return None
    
    def DateTime(self, *args, **kwargs):
        return None
    
    def Boolean(self, *args, **kwargs):
        return None
    
    def Text(self, *args, **kwargs):
        return None
    
    def Float(self, *args, **kwargs):
        return None
    
    def __getattr__(self, name):
        return lambda *args, **kwargs: None

db = DummyDB()  # 默认使用虚拟对象


# 创建SQLAlchemy实例
def CreateSQLAlchemy(app, type):
    global db

    try:
        # 选择开发 / 线上环境
        env = switch[type]

        # 将配置信息加载到 Flask 应用程序中
        app.config.from_object(env)

        # 保存起来，方便其他地方使用
        db = SQLAlchemy(app)
    except Exception as e:
        print(f"⚠ Failed to initialize SQLAlchemy: {e}")
        # 保持使用虚拟对象
        db = DummyDB()

    return db
