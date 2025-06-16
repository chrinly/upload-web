# 使用官方 Python 运行时作为父镜像
FROM --platform=linux/amd64 python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到容器内
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 创建上传和备份目录
RUN mkdir -p /app/uploadfiles /app/backup

# 设置环境变量（可选，防止Python缓存）
ENV UPLOAD_FOLDER=/app/uploadfiles
ENV BACKUP_FOLDER=/app/uploadfiles/backup

# 暴露端口
EXPOSE 5002

# 运行 Flask 应用
CMD ["python", "upload.py"]
