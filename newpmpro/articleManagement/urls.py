from django.conf.urls import url, include
from articleManagement.views import articlesListPage

urlpatterns = [
    url(r'', articlesListPage, name='articles-page')
]