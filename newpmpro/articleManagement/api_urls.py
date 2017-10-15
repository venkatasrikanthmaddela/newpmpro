from django.conf.urls import url, include
from articleManagement.api_views import VoteForTheArticle, SendArticleForReview, GetArticleRelModules

urlpatterns = [
    url(r'vote', VoteForTheArticle.as_view()),
    url(r'send-for-review', SendArticleForReview.as_view()),
    url(r'get-article-rel-modules', GetArticleRelModules.as_view())
]