from django.shortcuts import render

from django.http import HttpResponse
from blog.models import Article
# Create your views here.

def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    breif_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title: %s, breif_content: %s, content: %s, article_id: %s, publish_date: %s' % (title,breif_content,content,article_id,publish_date)
    return HttpResponse(return_str)

def get_index_page(request):
    all_article = Article.objects.all()
    return render(request, 'blog/index.html',
                {
                    'article_list': all_article
                }
                )

def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
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