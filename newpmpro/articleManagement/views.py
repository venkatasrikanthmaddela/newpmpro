from django.shortcuts import render
from newpmpro.models import Article


def articlesListPage(request):
    totalArticles = Article.objects.all()
    return render(request, 'articleManagement/articlesListPage.html', {"allArticles":totalArticles})