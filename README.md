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

## Carrie chen
复制

删除

我的这个项目已经提交到github了，你能帮我写个完善的readme介绍我这个项目吗，我的目的是为了向大家介绍这个项目，另一方面放在我的简历里面

## Trae AI
我很乐意帮你写一个完善的README来介绍你的项目。为了写出更有针对性的内容，我需要了解一些关于你项目的基本信息。请问你能提供以下信息吗？

1. 项目的名称是什么？
2. 项目的主要功能和目的是什么？
3. 使用了哪些主要技术栈？
4. 项目有哪些特色或创新点？
5. 项目的基本结构是怎样的？
6. 如何安装和运行这个项目？
有了这些信息，我就能为你写一个既适合项目介绍又适合放在简历中的专业README文档。

## Carrie chen
复制

删除

backend front 叫：职场女性健康管理平台，按照这些文档来写

## Trae AI
参考了 26 个上下文

# Sani - 职场女性健康管理平台
## 项目简介
Sani 是一个专为职场女性设计的健康管理平台，致力于解决女性在职场中面临的健康挑战，特别是经期和更年期健康问题。通过结合 AI 技术、个性化健康追踪和专业医疗资源对接，Sani 帮助女性更好地平衡工作与健康，同时为企业提供数据驱动的解决方案，减少缺勤率，提高生产力。

## 核心功能
### 1. 个性化周期追踪
- 智能月经周期预测 ：基于历史数据和机器学习算法，准确预测下一次月经周期时间
- 日历集成 ：将周期预测与个人日历集成，便于工作和生活安排
### 2. AI 健康助手 (Ask Sani)
- 24/7 即时健康咨询：回答与女性健康相关的各类问题，包括经期、更年期等
- 基于 Dify.AI 的智能对话系统
- 隐私保护的健康教育，以来大模型提供丰富的女性健康知识，并规范sani保护用户数据
- 个性化健康建议
### 3. 实时健康支持
- 医生预约系统
- 支持公司合作医生和私人医生预约
- 预约管理（查看、修改、取消）
- 医生资源库
### 4. 实时健康支持
- 个性化饮食推荐：根据你目前的状况推荐三天的饮食
### 5. 卫生用品管理（需要硬件支持）
- 卫生用品库存追踪
- 智能补货提醒
- 用品使用分析
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
### 后端部署
```bash
# 进入后端目录
cd sani-platform/backend

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
```bash
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

