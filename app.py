from src import CreateApp
from flask_cors import CORS
from flask import request, jsonify
from hashlib import md5

app = CreateApp("dev")

# 启用 CORS - 支持所有来源、所有方法、所有请求头
CORS(
    app,
    resources={
        r"/*": {
            "origins": "*",
            "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"],
            "supports_credentials": False,
            "max_age": 3600,
        }
    },
)

# Set default config if not present
if "PORT" not in app.config:
    app.config["PORT"] = 5000
if "DEBUG" not in app.config:
    app.config["DEBUG"] = True


@app.route("/")
def Home():
    return "Hello Flask!"


# 临时添加登录路由以绕过数据库连接问题
@app.route("/api/login", methods=["POST", "OPTIONS"])
def LoginTemp():
    if request.method == "OPTIONS":
        return "", 200

    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        # 临时硬编码登录用户
        if username == "liuyuyang" and password == "123123":
            import jwt
            from datetime import datetime, timedelta

            expire = app.config.get("EXPIRE", 10000)
            secretkey = app.config.get("SECRET_KEY", "LiuYuYang1024")
            algorithm = app.config.get("ALGORITHM", "HS256")

            payload = {"exp": datetime.utcnow() + timedelta(seconds=expire)}

            token = jwt.encode(payload, secretkey, algorithm)

            user = {
                "id": 1,
                "username": "liuyuyang",
                "name": "YuYang",
                "email": "3311118881@qq.com",
                "avatar": "https://q1.qlogo.cn/g?b=qq&nk=3311118881&s=640",
                "info": "再渺小的星光，也有属于他的光芒!",
                "role": "admin",
            }

            return jsonify(
                {
                    "code": 200,
                    "message": "登录成功",
                    "data": {"token": token, "user": user},
                }
            )
        else:
            return jsonify({"code": 400, "message": "登录失败：用户名或密码错误"}), 400
    except Exception as e:
        return jsonify({"code": 500, "message": f"服务器错误：{str(e)}"}), 500


if __name__ == "__main__":
    debug = app.config.get("DEBUG", True)
    port = app.config.get("PORT", 5000)

    print(f"Starting Flask server on http://0.0.0.0:{port}")
    print(f"API在线文档：http://127.0.0.1:{port}/docs")
    print("✓ CORS enabled for all origins")
    app.run(debug=debug, port=port, host="0.0.0.0")
