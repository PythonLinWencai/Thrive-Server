# Thrive-Server

> Python Flask 后端 API 服务

## 项目简介

Thrive-Server 是 Thrive 博客管理系统的后端服务，基于 Python Flask 框架开发，提供完整的 RESTful API 接口，支持用户管理、文章管理、评论系统等功能。

## 技术栈

- **框架**: Flask
- **数据库**: SQLAlchemy + MySQL
- **认证**: JWT
- **文档**: Flask-Siwadoc (自动生成 API 文档)
- **跨域**: Flask-CORS

## 环境要求

- Python 3.8+
- MySQL 5.7+ (可选，开发时可使用虚拟数据库)

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/LiuYuYang01/Thrive-Server.git
cd Thrive-Server
```

### 2. 创建虚拟环境

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置数据库 (可选)

编辑 `src/config/env.py` 中的数据库连接信息：

```python
# 开发环境配置
class DevelopConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost:3306/thrive"
```

### 5. 启动服务

```bash
python app.py
```

服务将在 `http://127.0.0.1:5000` 启动。

## API 文档

启动服务后，访问：
- API 文档: http://127.0.0.1:5000/docs
- 健康检查: http://127.0.0.1:5000/

## 项目结构

```
Thrive-Server/
├── app.py                 # Flask 应用入口
├── requirements.txt       # Python 依赖
├── src/
│   ├── __init__.py       # Flask 应用工厂
│   ├── config/           # 配置管理
│   ├── model/            # 数据模型
│   ├── router/           # API 路由
│   ├── service/          # 业务逻辑
│   └── utils/            # 工具函数
└── README.md
```

## 主要功能

- ✅ 用户认证与授权
- ✅ 文章管理 (增删改查)
- ✅ 评论系统
- ✅ 分类管理
- ✅ 文件上传
- ✅ 系统配置

## 开发说明

### 数据库迁移

```bash
# 进入虚拟环境后
from src import app
with app.app_context():
    db.create_all()
```

### 测试

```bash
python -m pytest
```

## 部署

### 使用 Docker

```bash
docker build -t thrive-server .
docker run -p 5000:5000 thrive-server
```

### 生产环境

1. 设置环境变量
2. 使用 Gunicorn 或 uWSGI
3. 配置反向代理 (Nginx)

## 贡献指南

1. Fork 项目
2. 创建功能分支: `git checkout -b feature/AmazingFeature`
3. 提交更改: `git commit -m 'Add some AmazingFeature'`
4. 推送分支: `git push origin feature/AmazingFeature`
5. 发起 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系方式

- 项目主页: https://github.com/LiuYuYang01/Thrive-Server
- 邮箱: liuyuyang1024@yeah.net

---

**开源不易，如果这个项目对你有帮助，请给个 Star ⭐ 支持一下！**

控制端：[LiuYuYang01/Thrive-Admin (github.com)](https://github.com/LiuYuYang01/Thrive-Admin)

后端：[LiuYuYang01/Thrive-Server (github.com)](https://github.com/LiuYuYang01/Thrive-Server)



这个项目从前端到后端都是我从0到1敲出来的，所以刚开始一定会有很多隐藏的 `BUG`，希望大家能够及时在 `GitHub` 反馈，这样我也好加以改正，不断改善，成为最佳！当然如果大家能够提交 `PR` 那再好不过了
