from django.shortcuts import render
from django.views import View
from logger import logger
from articleManagement.utils import get_article_data, article_review_check
from articleManagement.models import Article, Tags
from django.views import generic
from newpmpro.utils import get_log_string


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
    is_super_user = False
    try:
        if request.user.is_authenticated and request.user.is_superuser:
            article_review_check(*articles_list)
            is_super_user = True
    except Exception as e:
        logger.error(get_log_string('error: '+str(e)), exc_info=True)
    return render(request, 'articleManagement/articlePage.html', {"allArticles": articles_list,
                                                                  "isSuperUser": is_super_user})


