## 📦 项目简介：Web 文件上传系统

这是一个简单实用的 Web 文件上传系统，适合个人或团队快速部署使用，支持通过网页界面上传 ZIP 文件，自动备份旧文件，并提供 Docker 支持，方便迁移和部署。

### ✨ 功能特色

- **🌐 网页上传**
  - 通过浏览器即可上传 `.zip` 文件
  - 无需使用 FTP、SCP 或命令行，操作简单方便
  - 默认限制上传文件大小为 **50MB**

- **🛡️ 自动备份**
  - 如果上传文件与已有文件同名，系统会自动重命名原文件为备份并移入 `backup/` 目录
  - 备份文件名中包含时间戳，确保历史版本可追溯

- **📁 备份数量限制**
  - 每个文件最多保留最近 **3 个**备份版本
  - 超过的部分将自动删除最旧的备份，防止无限增长占用磁盘空间

- **🕒 上传时间显示**
  - 所有上传文件在网页界面会显示具体的上传时间，便于查找和管理

- **🐳 Docker 支持**
  - 提供 Dockerfile，可一键构建镜像
  - 可运行于任何支持 Docker 的服务器平台（Linux / Mac / Windows）

---
### 效果展示

<img width="1457" alt="image" src="https://github.com/user-attachments/assets/2bb6cfad-de1b-40a7-ae9c-63d7cfb631b8" />
<img width="1337" alt="image" src="https://github.com/user-attachments/assets/55d6d1de-7eab-44b5-a702-646c935f8347" />
<img width="446" alt="image" src="https://github.com/user-attachments/assets/a3fe1515-9a47-4135-b688-b701fd3ee13c" />


### 🚀 快速开始

使用 Docker 运行：
```bash
docker build -t upload-web .
docker run -d -p 8080:8080 upload-web
