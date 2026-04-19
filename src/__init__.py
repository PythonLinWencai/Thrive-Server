from flask import Flask

app = Flask(__name__, static_url_path="/")

# 创建虚拟的 siwa 对象以防止导入错误
class DummySiwa:
    def doc(self, *args, **kwargs):
        def decorator(func):
            return func
        return decorator

siwa = DummySiwa()

def CreateApp(env):
    try:
        from src.model import CreateSQLAlchemy
        db = CreateSQLAlchemy(app, env)

        # 在应用上下文中运行应用
        with app.app_context():
            # 创建所有继承自db.Model的表
            try:
                db.create_all()
                print("✓ Database tables created successfully")
            except Exception as e:
                print(f"⚠ Warning: Could not create database tables: {e}")
    except Exception as e:
        print(f"⚠ Warning: Could not initialize database: {e}")

    # 配置网站资源存放位置
    app.static_folder = app.config.get("UPLOAD_PATH", "/upload")[1:]

    # 加载路由 - 这是重要的，即使数据库连接失败也要加载
    try:
        from src import router
        print("✓ Routes loaded successfully")
    except Exception as e:
        print(f"⚠ Warning: Could not load router: {e}")

    return app
