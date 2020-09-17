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

注册文章模型
```
#suyun/blog/admin.py
from .models import Article

admin.site.register(Article)
```    
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
    
    >>>from blog.models import Article
    >>>art = Article()
    >>>art.title = 'Test Django Shell'
    >>>art.brief_content = 'Test Django Shell brief_content'
    >>>art.content = 'Test Django Shell Main content'
    >>>print(art)
    >>>Article object(None)
    >>>art.save()
    >>>
    >>>articles = Article.objects.all()
    >>>article = articles[0]
    >>>print(article.title)
    Test Django Shell
    >>>print(article.brief_content)
    Test Django Shell brief_content
    >>>print(article.content)
    Test Django Shell Main content
    
    >>>exit()

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
```
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
import blog.views

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
页面布局 bootstrap
##### 首页
![avatar][base64str]
[base64str]:data:image/png;base64,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

##### 详情页

#### 页面跳转
页面调整包括首页到详情页的跳转和本页向上一篇和下一遍文章的跳转两部分的跳转。
##### 首页详情页跳转


##### 本页向上下页面跳转

#### 分页功能

#### 最近文件列表

#### 评论