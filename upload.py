import os
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # 用于flash消息

# 配置上传文件夹
UPLOAD_FOLDER = '/app/uploadfiles'
ALLOWED_EXTENSIONS = {'zip'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 确保上传文件夹存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

BACKUP_FOLDER = '/app/uploadfiles/backup'
if not os.path.exists(BACKUP_FOLDER):
    os.makedirs(BACKUP_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # 检查是否有文件
        if 'file' not in request.files:
            flash('没有选择文件')
            return redirect(request.url)
        
        file = request.files['file']
        
        # 如果用户没有选择文件
        if file.filename == '':
            flash('没有选择文件')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if os.path.exists(save_path):
                name, ext = os.path.splitext(filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                backup_name = f"{name}_{timestamp}{ext}"
                backup_path = os.path.join(BACKUP_FOLDER, backup_name)
                os.rename(save_path, backup_path)
                # 只保留最近3份备份
                backups = []
                for f in os.listdir(BACKUP_FOLDER):
                    if f.startswith(f"{name}_") and f.endswith(ext):
                        parts = f[len(name)+1:-(len(ext))]
                        if len(parts) == 15 and parts[8] == '_' and parts.isdigit() == False:
                            backups.append(f)
                if len(backups) > 3:
                    backups.sort()
                    for old_backup in backups[:-3]:
                        os.remove(os.path.join(BACKUP_FOLDER, old_backup))
            file.save(save_path)
            flash('文件上传成功！')
            return redirect(url_for('upload_file'))
        else:
            flash('不允许的文件类型')
            return redirect(request.url)
    
    # 获取已上传的文件列表和上传时间
    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(filepath):
            upload_time = os.path.getmtime(filepath)
            files.append({'name': filename, 'upload_time': upload_time})
    # 按时间倒序排列
    files.sort(key=lambda x: x['upload_time'], reverse=True)
    return render_template('index.html', files=files)

@app.template_filter('datetimeformat')
def datetimeformat(value):
    return datetime.fromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
