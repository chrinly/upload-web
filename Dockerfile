# 使用官方 Python 运行时作为父镜像
FROM --platform=linux/amd64 python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到容器内
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 5002

# 运行 Flask 应用
CMD ["python", "upload.py"]
