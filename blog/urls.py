from django.urls import path, include
import blog.views

urlpatterns = [
    path('content', blog.views.article_content)
]