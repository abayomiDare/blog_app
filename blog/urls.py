from django.urls import path
from django.urls.conf import include
from.views import *


app_name = 'blog'

urlpatterns = [
    path('article/',article_list, name='article_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',article_detail, name='article_detail'),
    path('<int:post_id>/share/',article_share, name='article_share')
]