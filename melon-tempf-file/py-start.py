from dotenv import load_dotenv
import os

# 从 .env 文件加载环境变量
load_dotenv(dotenv_path="../.env")

# 访问 GITHUB_TOKEN 变量
github_token = os.getenv("GITHUB_TOKEN")

print(github_token)