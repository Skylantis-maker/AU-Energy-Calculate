# 澳大利亚储能收益预测系统

这是一个基于Flask的Web应用，用于计算和分析澳大利亚电力市场中储能系统的潜在收益。

## 功能特点

- 支持CSV和Excel格式的价格数据导入
- 提供单次充放电和两次充放电策略
- 自动计算最优充放电时间窗口
- 可视化展示每日和累计收益
- 展示价格差异和趋势分析
- 支持整月数据分析

## 技术栈

- 后端：Python Flask
- 数据处理：Pandas, NumPy
- 前端：HTML, CSS, JavaScript
- 图表：Plotly.js

## 安装说明

1. 克隆仓库：
```bash
git clone https://github.com/Skylantis-maker/AU-Energy-Calculate.git
cd AU-Energy-Calculate
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
python backend/app.py
```

应用将在 http://localhost:5002 运行

## 使用方法

1. 准备数据文件：
   - 支持CSV和Excel格式
   - 需要包含时间戳和价格两列
   - 时间戳格式：YYYY/M/D HH:MM
   - 时间间隔：5分钟

2. 选择策略：
   - 单次充放电：每天进行一次充电和放电
   - 两次充放电：每天进行两次充电和放电，获取更多收益

3. 上传文件并查看结果：
   - 显示每日收益和累计收益
   - 展示价格差异图表
   - 提供详细的充放电时间窗口

## 部署

项目已配置好Heroku部署所需的文件：
- Procfile
- requirements.txt
- runtime.txt

## 安全特性

- 请求频率限制
- 文件大小限制
- HTTPS强制启用
- 文件类型验证
- 自动清理上传文件

## 许可证

MIT License

## 作者

Skylantis-maker

## 更新日志

### 2024-04-18
- 优化了两次充放电策略的计算逻辑
- 改进了错误处理和日志输出
- 添加了安全特性和部署配置 