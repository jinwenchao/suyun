from django.db import models

# Create your models here.
class Article(models.Model):
    # 文章唯一ID
    article_id = models.AutoField(primary_key=True)
    # 标题
    title = models.CharField(max_length=200)
    # 摘要
    brief_content = models.TextField()
    # 内容
    content = models.TextField()
    # 发布日期
    publish_date = models.DateTimeField(auto_now=True)
