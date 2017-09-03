from django.conf.urls import url, include
from articleManagement.api_views import VoteForTheArticle

urlpatterns = [
    url(r'vote', VoteForTheArticle.as_view())
]