from django.shortcuts import render
from newpmpro.models import Article, Categories, Tags, HyperLinks


def articlesListPage(request):
    articles_list = list()
    totalArticles = Article.objects.all()
    for each_article in totalArticles:
        categories_list = Categories.objects.filter(articleId=each_article.id).values_list('name', flat=True)
        tags_list = Tags.objects.filter(articleId=each_article.id).values_list('tagName', flat=True)
        links_list = HyperLinks.objects.filter(articleId=each_article.id)
        article_data = {"categories": [],
                        "tags": [],
                        "links": [],
                        "articleData": {}
                        }
        if categories_list:
            for each_category in categories_list:
                article_data["categories"].append(each_category)
        if tags_list:
            for each_tag in tags_list:
                article_data["tags"].append(each_tag)
        if links_list:
            for each_link_data in links_list:
                article_data["links"].append(
                    {
                        "linkName": each_link_data.linkName,
                        "link": each_link_data.link
                    }
                )
        article_data["articleData"] = each_article
        articles_list.append(article_data)
    return render(request, 'articleManagement/articlesListPage.html', {"allArticles":articles_list})