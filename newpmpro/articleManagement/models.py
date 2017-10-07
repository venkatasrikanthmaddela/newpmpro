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

    @classmethod
    def get_model_field_names(cls):
        fields_list = list()
        for each_field in Article._meta.fields:
            if each_field.attname not in CustomModel.get_field_names():
                fields_list.append(each_field.attname)
        return fields_list

    def create_article(self, article_data):
        try:
            self.title = article_data.get("title")
            self.subTitle = article_data.get("subTitle")
            self.content = article_data.get("content")
            self.codePart = article_data.get("codePart")
            self.author = article_data.get("author_id")
            self.isActive = article_data.get("isActive")
            self.save()
            return "success"
        except Exception as e:
            return "error"

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
