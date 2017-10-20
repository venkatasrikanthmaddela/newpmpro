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
            return self
        except Exception as e:
            return "error"


class Tags(CustomModel):
    tagName = models.CharField(max_length=256)

    def save_tag(self, tag):
        try:
            tag_info = Tags.objects.get(tagName=tag)
            return tag_info
        except Tags.DoesNotExist:
            self.tagName = tag
            self.save()
            return self


class Categories(CustomModel):
    name = models.CharField(max_length=256)

    def save_category(self, category):
        try:
            category_info = Categories.objects.get(name=category)
            return category_info
        except Categories.DoesNotExist:
            self.name = category
            self.save()
            return self


class ArticleRelatedTags(CustomModel):
    articleId = models.ForeignKey(Article)
    tag = models.ForeignKey(Tags)

    def map_article_with_tags(self, article_id, tag_id):
        try:
            self.articleId = Article.objects.get(id=article_id)
            self.tag = Tags.objects.get(id=tag_id)
            self.save()
            return self
        except:
            return "error"


class ArticleRelatedCategories(CustomModel):
    articleId = models.ForeignKey(Article)
    category = models.ForeignKey(Categories)

    def map_article_with_category(self, article_id, category_id):
        try:
            self.articleId = Article.objects.get(id=article_id)
            self.category = Categories.objects.get(id=category_id)
            self.save()
            return self
        except:
            return "error"


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

