# 📝 Calendar-Todolist

> 一个基于Django创建的日历导向型**待做清单**

## 🎯 项目简介

- 项目起源:一个觉得自己行了的Django初学者听了姐姐的建议,做一个可以日常用的待做清单证明自己
- 项目提供了一个账号的登入和注册方便云端储存待做清单
- 在登入界面用户可以选择免登录版和登入版导致清单
- 免登录版是AI生成的简单的待做清单(本地保存,无日历)
- 登入后就可以进入带日历的待做清单(没错,也是靠AI做出来的)
- 不要问我为什么那么多AI做的东西,问就是菜,还得靠AI(不要骂了😭)

## 🛠️ 技术栈

### 后端
- **框架**: Django框架
- **数据库**: SQLite3
- **图表生成**: base64编码图片嵌入
- **数据处理与可视化**: numpy + matplotlib 

### 前端
- **技术**：HTML5 + CSS + JavaScript
- **样式**：CSS-in-JS (Tailwind配置)
- **交互**：JavaScript原生实现
- **主题**：明暗双主题

## 📦 安装部署

### 环境要求
- python >=  3.10.16
- Django >=  5.2.2
- numpy >=  2.2.6
- matplotlib >= 3.10.6

### 安装步骤

1. **克隆项目**
   ```bash
   git clone [你的项目地址]
   cd [项目文件夹名]
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或者
   venv\Scripts\activate  # Windows
   #或者使用anaconda创建虚拟环境并激活虚拟环境
   conda create --name 环境名称 python=版本号
   conda activate 环境名称
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **数据库配置**
   ```bash
   cd [Django项目目录]
   python manage.py makemigrations 
   python manage.py migrate  
   ```

5. **启动项目**

   ```bash
   cd [Django项目目录]
   python manage.py runserver 
   ```

6. **创建管理员(可选)**

   ```bash
   python manage.py createsuperuser
   #后台管理地址为127.0.0.1:8000/admin
   #可对user和task进行修改等操作
   ```

## 📁 项目结构

在这里描述项目的目录结构：
```
Django项目目录
├── 📄 README.md                    # 项目说明文档
├── 📄 db.sqlite3                   # SQLite数据库文件
├── 📄 manage.py                    # Django项目管理脚本
├── 📄 记录文档.txt                 # 项目记录文档(记录我的创作过程)
│
├── 📁 todolist\                    # 主项目配置目录
│   ├── 📄 __init__.py
│   ├── 📄 asgi.py                  # ASGI配置
│   ├── 📄 settings.py              # Django设置文件
│   ├── 📄 urls.py                  # 主URL路由配置
│   └── 📄 wsgi.py                  # WSGI配置
│
├── 📁 index\                       # 任务管理应用
│   ├── 📄 __init__.py
│   ├── 📄 admin.py                 # Django管理后台配置
│   ├── 📄 apps.py                  # 应用配置
│   ├── 📄 mathimage.py             # 数学图表生成模块
│   ├── 📄 models.py                # 数据模型定义
│   ├── 📄 test_excel.py            # Excel测试文件
│   ├── 📄 tests.py                 # 单元测试
│   ├── 📄 urls.py                  # 应用URL路由
│   ├── 📄 views.py                 # 视图函数（包含统计图表功能）
│   │
│   ├── 📁 migrations\...           # 数据库迁移文件
│   │
│   ├── 📁 static\                    # 静态文件
│   │   └── 📁 image\
│   │       └── 📄 lookingphone.jpg # 背景图片
│   │
│   └── 📁 templates\               # HTML模板文件
│       ├── 📄 home.html              # 首页模板
│       └── 📄 index.html             # 主日历界面模板（1434行代码）
│
├── 📁 static\                        # 全局静态文件
│   ├── 📁 css\
│   │   └── 📄 custom.css             # 自定义CSS样式
│   ├── 📁 image\
│   │   └── 📄 todo.ico               # 网站图标
│   └── 📁 js\                        # JavaScript文件目录（空）
│
└── 📁 welcome\                       # 用户认证应用
    ├── 📄 __init__.py
    ├── 📄 admin.py                   # 用户管理后台
    ├── 📄 apps.py                    # 应用配置
    ├── 📄 function.py                # 用户相关功能函数
    ├── 📄 models.py                    # 用户数据模型
    ├── 📄 tests.py                     # 单元测试
    ├── 📄 urls.py                      # 认证URL路由
    ├── 📄 views.py                     # 登录注册视图
    │
    ├── 📁 migrations\...               # 用户表迁移文件
    │
    └── 📁 templates\                   # 认证页面模板
        ├── 📄 404.html                 # 错误页面
        ├── 📄 login.html               # 登录页面
        └── 📄 register.html            # 注册页面
```

## 🔧 核心功能说明

### 1.查看某天任务列表
点击日历里面的具体日期查看当天的所有任务,并有添加功能,点击任务可以就行修改和删除操作

![imagetxt1](https://github.com/atulearning/todolist/blob/main/readmefile/2025-09-24%20083005.png)

### 2.数据可视化
点击***完成统计***查看近7天的,与近30天的一个简单的数据统计图

![imagetxt2](https://github.com/atulearning/todolist/blob/main/readmefile/2025-09-24%20083621.png)

### 3.导出当天任务的excel表格

点击***导出任务到excel***就下载当前日期下任务的excel表格

![imagetxt3](https://github.com/atulearning/todolist/blob/main/readmefile/2025-09-24%20091124.png)

## 🚀 API接口

### 用户认证接口 (welcome/)

| 接口路径 | 请求方式 | 功能说明 | 请求参数 | 响应说明 |
|:--------|---------|----------|----------|----------|
| /welcome/login/ | POST | 用户登录 | username/email, password | 成功返回登录成功消息 |
| /welcome/register/ | POST | 用户注册 | username, email, password | 成功返回注册成功消息 |
| /welcome/check_username/ | GET | 检查用户名是否存在 | username | 返回exists: true/false |
| /welcome/check_email/ | GET | 检查邮箱是否存在 | email | 返回exists: true/false |
| /welcome/logout/ | GET | 用户注销 | 无 | 返回登录页面 |
| /welcome/protected/ | GET | 受保护的用户信息 | 无 | 需要登录状态 |

### 任务管理接口 (index/)

| 接口路径 | 请求方式 | 功能说明 | 请求参数 | 响应说明 |
|:--------|---------|----------|----------|----------|
| /index/get_user_info/ | GET | 获取当前用户信息 | 无 | 返回用户名 |
| /index/get_task/ | POST | 获取指定日期任务 | date (YYYY-MM-DD) | 返回任务列表 |
| /index/add_task/ | POST | 添加新任务 | title, date | 返回任务ID和成功消息 |
| /index/delete_task/ | POST | 删除任务 | id (任务ID) | 返回删除成功消息 |
| /index/update_task/ | POST | 更新任务 | id, title, completed | 返回更新成功消息 |
| /index/complete_task/ | POST | 标记任务完成状态 | id, completed | 返回状态更新消息 |
| /index/total_image/ | POST | 获取任务统计图表 | 无 | 返回7天和30天统计图表 |
| /index/export_tasks_excel/ | POST | 导出任务到Excel | 无 | 返回Excel文件下载 |

## 🔍 使用示例

### 示例1：用户登录
```javascript
// 用户登录
fetch('/welcome/login/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        username: 'testuser',  // 或者使用 email: 'test@example.com'
        password: 'password123'
    })
})
.then(response => response.json())
.then(data => {
    if (data.message) {
        console.log('登录成功:', data.message);
    } else {
        console.error('登录失败:', data.error);
    }
});
```

### 示例2：获取任务列表
```javascript
// 获取指定日期的任务
fetch('/index/get_task/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        date: '2024-01-15'  // 日期格式：YYYY-MM-DD
    })
})
.then(response => response.json())
.then(tasks => {
    console.log('任务列表:', tasks);
    // tasks 格式: [{id: 1, title: '任务1', completed: false, date: '2024-01-15'}, ...]
});
```

### 示例3：添加新任务
```javascript
// 添加新任务
fetch('/index/add_task/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        title: '完成项目文档',
        date: '2024-01-15'
    })
})
.then(response => response.json())
.then(data => {
    if (data.message) {
        console.log('任务添加成功，任务ID:', data.id);
    } else {
        console.error('添加失败:', data.error);
    }
});
```

### 示例4：获取任务统计图表
```javascript
// 获取任务统计图表数据
fetch('/index/total_image/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    }
})
.then(response => response.json())
.then(data => {
    if (data.message) {
        console.log('图表生成成功');
        // data.d7_image 包含7天统计图表
        // data.d30_image 包含30天统计图表
        document.getElementById('chart7').src = 'data:image/png;base64,' + data.d7_image;
        document.getElementById('chart30').src = 'data:image/png;base64,' + data.d30_image;
    } else {
        console.error('生成失败:', data.error);
    }
});
```

## 📈 性能优化

- ⚡ 加载速度优化
- 💾 数据库优化
- 🔄 缓存策略:用户数据存储在服务端的数据库中,图片数据等靠内存直接传输不占用空间

## 📝 开发日志

```txt
--2025.9.18
----工作日志
    1.添加了导出excel的功能
    2.改善了一下页面布局
----问题部分
    1.手机端布局适配偶尔有点问题
#具体进展见记录文档
```



### 更新日期 (2025-9-24)
- ✨ 初始版本发布
- 🎯 实现了核心功能
- 🐛 修复了已知问题

### 更新计划
- 🚀 计划添加用户修改密码的功能
- 🔧 计划优化现有功能
- ✏️计划完成自己对新功能想法的实现

### **现存问题**

- 并没有对数据获取进行加密和反扒处理
- 登入也就做了简单的跳过登入处理,cookie,session等没怎么用
- 现在项目处于开发阶段,距离投入使用还有很长的距离,如果你想投入使用,你可以进行修改

## 🤝 贡献指南(给点建议吧)

欢迎提交Issue和Pull Request！

### 如何贡献
1. Fork 这个项目
2. 创建你的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📄 许可证

- MIT License - 详细请见License

---

## ⭐ Star History

如果项目有帮助，请给个Star支持一下！

[![Star History Chart](https://api.star-history.com/svg?repos=[atulearning]/[tdolist])](https://star-history.com/#[atulearning]/[tdolist])

---

**🎉 感谢使用 [tdolist]！** 


> 💡 **小贴士**：边学边做,敢于突破!请大佬们轻点骂(●'◡'●),我会努力完善这个项目的



