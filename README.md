"# sunyun"
## 环境说明
|  标识   |  软件 |  版本  |  说明  |
|  ----  | ----  | ----  | ----  |
| 1  | system |  windows10  |  家庭中文版  |
| 2  | python |  3.8.5  |  开发语言  |
| 3  | django |  3.1.0  |  框架名称  | 
| 4  | pycharm |  2002.2  |  IDE  | 
| 5  | git |  2.25.1  |  代码管理工具  | 
| 6  | PowerShell |  5.1.19041.1  |  执行命令工具  |  
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
- 博客系统
- 投票系统
- 论坛系统
- 员工信息
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

页面布局

1.suyun/blog文件夹下创建templates文件夹

2.文件夹下创建index.html

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Django Web</title>
  <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</head>
<body>
  <div class="container page-header">
    <h1>First Django Article
      <small>---by shalter</small>
    </h1>
  </div>
  <div class="container page-body">
    <div class="col-md-9" role="main">
      <div class="body-main">
        {% for article in article_list %}
        <div>
          <h2><a href="/blog/detail/{{article.article_id}}">{{ article.title }}</a></h2>
          <p>
            {{ article.brief_content }}
          </p>
        </div>
        {% endfor %}
      </div>
    <div>
    <div class="col-md-3" role="complementary">
      <div>
        <h2>最新文章</h2>
        {% for article in article_list %}
        <h4><a href="/blog/detail/{{article.article_id}}">{{ article.title }}</a></h4>
        {% endfor%}
      </div>
    </div>
  </div>
</body>
</html>
```

article_list 文章列表数据
```
# suyun/blog/views.py
def get_index_page(request):
    all_article = Article.objects.all()
    return render(request, 'blog/index.html',
                {
                    'article_list': all_article    
                }
                )
```

suyun/blog/templates文件夹下创建blog文件夹，将index.html和detail.html迁移进去

路由配置
```
#suyun/blog/urls.py
urlpatterns = [
    ...    
    path('index', blog.views.get_index_page),
```

运行项目后，浏览器中输入

    http://127.0.0.1:8000/blog/index
    
##### 详情页

文件夹下创建detail.html

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Django Web</title>
  <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</head>
<body>
  <div class="container page-header">
    <h1>{{ curr_article.title }}
    </h1>
  </div>
  <div class="container body-main">
    <div>
      {% for section in section_list %}
      <p>
        {{ section }}
      </p>
      {% endfor %}
    <div>
  </div>
</body>
</html>
```

文件详情页数据
```
#suyun/blog/views
def get_detail_page(request):
    curr_article = Article.objects.all()[0]
    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
                {
                    'curr_article': curr_article,
                    'section_list': section_list    
                }
                )
```

路由配置
```
#suyun/blog/urls.py
urlpatterns = [
    ...    
    path('detail', blog.views.get_detail_page),
```

运行项目后，浏览器中输入

    http://127.0.0.1:8000/blog/detail
    
模板系统渲染

#### 页面跳转
页面调整包括首页到详情页的跳转和本页向上一篇和下一遍文章的跳转两部分的跳转。
##### 首页详情页跳转
修改路由
```
#suyun/blog/urls.py
path('detail', blog.views.get_detail_page),
调整为:
path('detail/<int:article_id>', blog.views.get_detail_page),
```
改造get_detail_page()函数
```
#suyun/blog/views.py
def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    for article in all_article:
      if article.article_id == article_id:
        curr_article = article
        break
    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
                {
                    'curr_article': curr_article,
                    'section_list': section_list    
                }
                )
```    
在suyun/blog/templates/blog/index.html中修改如下
```
<h2><a href="/blog/detail/{{article.article_id}}">{{ article.title }}</a></h2>
<h4><a href="/blog/detail/{{article.article_id}}">{{ article.title }}</a></h4>
```
##### 本页向上下页面跳转
页面按钮元素添加
```
#suyun/blog/templates/blog/detail.html
...
<div>
    <nav aria-label="...">
      <ul class="pager">
        <li><a href="/blog/detail/{{ previous_article.article_id }}">上一篇: {{ previous_article.title }}</a></li>
        <li><a href="/blog/detail/{{ next_article.article_id }}">下一篇: {{ next_article.title }}</a></li>
      </ul>
    </nav>
</div>
</body>
```

数据传递

通过当前文章的下标去查找上一篇和下一篇
```
#suyun/blog/views.py
def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index,article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index -1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1

        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
                {
                    'curr_article': curr_article,
                    'section_list': section_list,
                    'previous_article': previous_article,
                    'next_article': next_article
                }
                )
```
#### 分页功能
```
#suyun/blog/templates/blog/index.html
...
    {% endfor %}
</div>
<div class="body-footer>
  <div class="col-md-4 col-md-offset -3">
    <nav aria-label="Page navigation">
      <ul class="pagination">
        <li>
          <a href="#" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <li><a href="#">1</a></li>
        <li><a href="#">2</a></li>
        <li><a href="#">3</a></li>
        <li><a href="#">4</a></li>
        <li><a href="#">5</a></li>
        <li>
          <a href="#" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</div>
```

获取页码
```hgignore
# suyun/blog/views
def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    print('page param:',paeg)
```

导入分页模块
```
#suyun/blog/views
from django.core.paginator import Paginator

def get_index_page(request):
    ...
    all_article = Article.objects.all()    
    paginator = Paginator(all_article,3)
    page_num = paginator.num_pages
    print('page num:',page_num)
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    return render(request, 'blog/index.html',
                {
                    'article_list': page_article_list
                    'page_num': range(1, page_num + 1)
                    'curr_page': page,
                    'next_page':next_page,
                    'previous_page':previous_page
                }
                )
```

修改页面
```
#suyun/blog/templates/blog/index.html
      <li>
          <a href="/blog/index?page={{ previous_page }}" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
      </li>
      {% for num in page_num %}
      <li><a href="/blog/index?page={{num}}">{{ num }}</a></li>
      {% endfor %}
      <li>
        <a href="/blog/index?page={{ next_page }}" aria-label="Next">
          <span aria-hidden="true">&raquo;</span>
        </a>
      </li>
        
```
#### 最近文件列表
倒叙排列最近的5篇文章

```
#suyun/blog/views.py
all_article = Article.objects.all()
top5_article_list = Article.objects.order_by('-publish_date')[:5]

    return render(request, 'blog/index.html',
                {
                    'article_list': page_article_list
                    'page_num': range(1, page_num + 1)
                    'curr_page': page,
                    'next_page':next_page,
                    'previous_page':previous_page,
                    'top5_article_list': top5_article_list
                }
                )
```
#### 评论
暂无开发该功能