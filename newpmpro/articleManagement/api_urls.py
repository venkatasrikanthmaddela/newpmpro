from django.conf.urls import url, include
from articleManagement.api_views import VoteForTheArticle, SendArticleForReview

urlpatterns = [
    url(r'vote', VoteForTheArticle.as_view()),
    url(r'send-for-review', SendArticleForReview.as_view())
]