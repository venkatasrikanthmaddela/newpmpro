from newpmpro.baseModels import CustomModel
from django.db import models
from newpmpro.models import PmUser, ProjectData


class Article(CustomModel):
    title = models.TextField()
    subTitle = models.TextField(default=None)
    content = models.TextField()
    codePart = models.TextField(default=None)
    author = models.ForeignKey(PmUser)
    isActive = models.BooleanField(default=True)


class Tags(CustomModel):
    tagName = models.CharField(max_length=256)


class ArticleRelatedTags(CustomModel):
    articleId = models.ForeignKey(Article)
    tag = models.ForeignKey(Tags)


class Categories(CustomModel):
    articleId = models.ForeignKey(Article)
    name = models.CharField(max_length=256)


class HyperLinks(CustomModel):
    articleId = models.ForeignKey(Article)
    linkName = models.TextField()
    link = models.URLField()


class ArticleFeedBack(CustomModel):
    article = models.ForeignKey(Article, default=None)
    user = models.ForeignKey(PmUser, default=None)
    likeCount = models.IntegerField(default=0)


class ArticleRequests(CustomModel):
    user = models.ForeignKey(PmUser, default=None)
    article = models.ForeignKey(Article, default=None)
    requestStatus = models.TextField(default='REQUESTED')

