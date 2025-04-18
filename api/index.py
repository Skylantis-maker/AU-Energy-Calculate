from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='../frontend')

# 服务静态文件
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# 导入后端应用的路由
from backend.app import upload_file, too_large, ratelimit_handler

# 注册路由
app.route('/api/upload', methods=['POST'])(upload_file)
app.errorhandler(413)(too_large)
app.errorhandler(429)(ratelimit_handler)

# Vercel handler
def handler(request):
    return app 