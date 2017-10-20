from django.shortcuts import render
from django.views import View
from articleManagement.utils import get_article_data
from articleManagement.models import Article, Tags
from django.views import generic


class ArticlesListPage(generic.ListView):
    model = Article
    context_object_name = "articles_list"
    queryset = Article.objects.all()
    template_name = 'articleManagement/articlesListPage.html'

    def get_context_data(self, **kwargs):
        context = super(ArticlesListPage, self).get_context_data(**kwargs)
        context["top_articles"] = Article.objects.all()[:20]
        context["top_tags"] = Tags.objects.all()[:20]
        return context


def post_article_page(request):
    return render(request, 'articleManagement/postArticle.html')



def article_page(request):
    article_id = request.GET.get("article-id")
    articles_list = get_article_data(article_id, request)
    return render(request, 'articleManagement/articlePage.html', {"allArticles": articles_list})