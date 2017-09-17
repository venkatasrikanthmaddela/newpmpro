

# article data utils
from articleManagement.models import Article, Categories, Tags, HyperLinks, ArticleFeedBack, PmUser, ArticleRelatedTags


def get_article_data(article_id, request=None):
    """

    :param article_id:
    :param request:
    :return: returns the whole aricle data for the given article id, the request param is optional
    """
    articles_list =  list()
    article_data = {"categories": [],
                    "tags": [],
                    "links": [],
                    "articleData": {},
                    "votesData": {}
                    }
    isVoted = False
    each_article = Article.objects.get(id=article_id)
    categories_list = Categories.objects.filter(articleId=each_article.id).values_list('name', flat=True)
    tags_list = ArticleRelatedTags.objects.filter(articleId=each_article.id).values_list('tag__tagName', flat=True)
    links_list = HyperLinks.objects.filter(articleId=each_article.id)
    votes_list = ArticleFeedBack.objects.filter(article=each_article)
    if request:
        try:
            user_object = PmUser.objects.get(email=request.user.email)
            users_lists_for_votes = list()
            for votes_data in votes_list:
                users_lists_for_votes.append(votes_data.user)
            if user_object in users_lists_for_votes:
                isVoted = True
        except:
            isVoted = False
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
    if votes_list:
        article_data["votesData"] = {
            "totalVotes": len(votes_list),
            "isVoted": isVoted
        }
    article_data["articleData"] = each_article
    articles_list.append(article_data)

    return articles_list


