from src.config import BaseConfig
from urllib.parse import quote

# 使用 urllib.parse.quote 正确编码特殊字符
password = quote("Lwc123!@#", safe='')

# 开发环境
class DevelopConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{password}@127.0.0.1:3306/ThriveX'


# 生产环境
class ProduceConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{password}@127.0.0.1:3306/ThriveX'


# 选择环境
switch = {
    "dev": DevelopConfig,
    "pro": ProduceConfig
}
