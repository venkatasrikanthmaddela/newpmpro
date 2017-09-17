from django.conf.urls import url, include
from articleManagement.views import article_page, ArticlesListPage, post_article_page

urlpatterns = [
    url(r'see-article', article_page, name='article-page'),
    url(r'post-article', post_article_page, name='post-article'),
    url(r'', ArticlesListPage.as_view(), name='articles-list-page')
]