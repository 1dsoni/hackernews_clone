from django.urls import path
from .views import signup, delete_article, undelete_article
from .views import read_article, deleted_articles_view, index_view

app_name = "dashboard"

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('delete/<int:article_id>', delete_article, name='delete'),
    path('undelete/<int:article_id>', undelete_article, name='undelete'),
    path('read/<int:article_id>', read_article, name='read'),
    path('deleted_articles/', deleted_articles_view, name='deleted_articles'),
    path('', index_view, name='home' ),

]
