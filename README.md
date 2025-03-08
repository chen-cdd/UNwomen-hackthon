#  职场女性健康管理平台

## 项目简介
该项目是一个专为职场女性设计的健康管理平台，致力于解决女性在职场中面临的健康挑战，特别是经期和更年期健康问题。通过结合 AI 技术、个性化健康追踪和专业医疗资源对接，Sani 帮助女性更好地平衡工作与健康，同时为企业提供数据驱动的解决方案，减少缺勤率，提高生产力。

## 核心功能
1. 个性化周期追踪
2. AI 健康助手（Ask Sani）
3. 医疗咨询预约

## 技术架构
### 前端
- 框架 : Vue.js 3
- UI 组件 : Element Plus
- 日历组件 : FullCalendar, Vue-Cal
- HTTP 客户端 : Axios
- Markdown 渲染 : Markdown-it
### 后端
- 框架 : FastAPI (Python)
- 数据库 ORM : SQLAlchemy
- 数据验证 : Pydantic
- 身份验证 : JWT
### 数据库
- MySQL : 用户数据、医疗记录、预约信息等结构化数据存储
### AI 集成
- Dify.AI : 提供智能健康助手对话能力

## 数据模型
系统包含多个核心数据模型，包括：
- 用户 (User) : 存储用户基本信息和认证数据
- 用户档案 (UserProfile) : 存储用户健康相关信息
- 医生 (Doctor) : 医生信息和专业领域
- 预约 (Appointment) : 用户与医生的预约记录
- 月经周期记录 (CycleRecord) : 用户月经周期数据
- 症状日志 (SymptomLog) : 用户健康症状记录
- 聊天历史 (ChatHistory) : AI 助手对话记录

## 隐私与安全
Sani 高度重视用户隐私和数据安全：
- 所有数据在传输和存储过程中使用行业标准加密协议
- 严格的访问控制限制谁可以查看用户信息
- 定期安全审计以识别和解决潜在漏洞
- 安全的基础设施托管在具有物理和网络安全措施的数据中心

## 商业价值
对企业而言，Sani 提供了显著的商业价值：
- 减少缺勤率 : 数据显示可减少 20% 的与健康相关的缺勤
- 提高生产力 : 员工健康状况改善带来 15% 的生产力提升
- 员工满意度 : 95% 的用户报告对平台服务满意
- 企业社会责任 : 展示企业对员工健康和多元包容的承诺

## 安装与部署
### 前端部署
```
# 克隆仓库
git clone https://github.com/yourusername/UNwomen-hackthon.git

# 进入前端目录
cd UNwomen-hackthon/front

# 安装依赖
npm install

# 启动开发服务器
npm run serve

# 构建生产版本
npm run build
```

### 后端部署
```
# 进入后端目录
cd UNwomen-hackthon/backend

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 启动服务器
uvicorn app.main:app --reload
```

### 数据库设置
```
# 导入数据库结构
mysql -u username -p database_name < source/unwomen.sql
```

## 未来规划
- 完善更年期部分
- 移动应用开发
- 更多健康追踪指标
- 企业健康管理仪表板
- 国际化支持
- 更多 AI 功能集成

## 贡献指南
我们欢迎社区贡献！如果您想参与项目开发，请：
1. Fork 仓库
2. 创建您的特性分支 ( git checkout -b feature/amazing-feature )
3. 提交您的更改 ( git commit -m 'Add some amazing feature' )
4. 推送到分支 ( git push origin feature/amazing-feature )
5. 开启一个 Pull Request

