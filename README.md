"# sunyun"
## 环境说明
|  标识   |  软件 |  版本  |  说明  |
|  ----  | ----  | ----  | ----  |
| 1  | system |  windows10  |  家庭中文版  |
| 2  | python |  3.8.5  |  开发语言  |
| 2  | django |  3.1.0  |  框架名称  | 
| 2  | pycharm |  2002.2  |  IDE  | 
| 2  | git |  2.25.1  |  代码管理工具  | 
| 2  | PowerShell |  5.1.19041.1  |  执行命令工具  |  
## 创建 suyun 项目
    django-admin startproject suyun
## 创建博客应用
    django-admin startapp blog
## 运行项目
    
    python manage.py runserver
    
###全局设置
设置时区
```
# suyun/suyun/settings.py
TIME_ZONE = 'Asia/Shanghai'
```
## 开发阶段
开发阶段包括:
- 博客开发
- 投票开发
- 论坛开发
### 博客开发

#### 模型创建
* 标题
* 摘要
* 内容
* 标识
* 日期


|  标识   | 字段  |  类型  |  说明  |
|  ----  | ----  | ----  | ----  |
| 1  | article_id |  IntegerField  |  AutoField  |
| 2  | title |  CharField  |  文章标题  |
| 3  | brief |  TextField  |  文章摘要  | 
| 4  | content |  TextField  |  文章内容  | 
| 5  | title |  DateTimeField  |  发布日期  | 
| 6  | title |  CharField  |  文章标题  |  

模型定义

    ```
    # suyun/blog/models.py
    class Article(models.Model):
        # 文章唯一ID
        article_id = models.AutoField(primary_key=True)
        # 文章标题
        title = models.CharField(max_length=200)
        # 文章摘要
        brief_content = models.TextField()
        # 文章内容
        content = models.TextField()
        # 发布日期
        publish_date = models.DateTimeField(auto_now=True)
    ```
模型迁移

    python manage.py makemigrations
创建迁移文件
    
    suyun\blog\migrations\0001_initial.py
    - Create model Article
    
数据迁移

    python manage.py migrate
    
验证模型
>使用django shell 验证
>
>便捷的验证模型
>
>小范围debug测试
>
步骤:

1.进入django shell

    python manage.py shell
    
2.创建一篇文章
    
    >>>from blog.models imprt Article
    >>>art = Article()
    >>>art.title = 'Test Django Shell'
    >>>art.brief = 'Test Django Shell brief_content'
    >>>art.content = 'Test Django Shell Main content'
    >>>print(art)
    >>>Article object(None)
    >>>art.save()
    >>>
    >>>articles = Article.objects.all()
    >>>article = articles[0]
    >>>print(article.title
    Test Django Shell
    >>>print(article.brief_content)
    Test Django Shell brief_content
    >>>print(article.content)
    Test Django Shell Main content

#### 管理台页面
>Django后台管理工具
>
>读取定义的模型元数据，提供管理页面
>
>基础设施
>
>认证用户、显示管理模型、校验输入
>
使用:
- 创建管理员用户
- 登陆管理页面
创建管理员用户
    
        
    python manage.py createsuperuser
         
    Username:shalter
    
    Email address:
    
    Password:Jx123!@#
    
    Password (again):Jx123!@#
    
    Superuser created successfully.
    
#### 运行项目
    python manage.py runserver
    
chrome浏览器中打开

    http://127.0.0.1:8080
    
Article 模型注册到Admin中
```buildoutcfg
# suyun/blog/admin.py
from .models import Article

admin.site.register(Article)
```
管理模块中显示文章标题
```
#suyun/blog/models.py
class Article(models.Model):
    ...    
    def __str__(self):
        return self.title
```
应用注册到项目
```
#suyun/suyun/settings.py
INSTALLED_APPS = [
    ...,
    'blog',

```
重新运行项目

    python manage.py runserver
刷新页面

#### 视图创建
数据页面调用
```
# suyun/blog/views.py
frome django.http import HttpResponse
from blog.models import Article

def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title: %s, brief_content: %s, content: %s, article_id: %s, publish_date: %s' % (title,brief_content,content,article_id,publish_date)
    return HttpResponse(return_str)
```
配置路由
1.应用级别路由配置
```
# suyun/blog/urls.py
from django.urls import path, include
from blog.views

urlpatterns = [
    path('content', blog.views.article_content)
]
```
2.项目级别路由配置
```
#suyun/suyun/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]
```
浏览器验证
http://127.0.0.1:8080/blog/content
#### 视图模板

#### 详情页

#### 页面跳转
页面调整包括首页到详情页的跳转和本页向上一篇和下一遍文章的跳转两部分的跳转。
##### 首页详情页跳转

##### 本页向上下页面跳转

#### 分页功能

#### 最近文件列表

#### 评论