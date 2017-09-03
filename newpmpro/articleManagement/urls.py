from django.conf.urls import url, include
from articleManagement.views import article_page, ArticlesListPage

urlpatterns = [
    url(r'see-article', article_page, name='article-page'),
    url(r'', ArticlesListPage.as_view(), name='articles-list-page')
]