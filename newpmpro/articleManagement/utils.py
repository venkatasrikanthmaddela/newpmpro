
# article data utils
from articleManagement.constants import ARTICLE_RELATED_MODULES
from articleManagement.models import Article, Categories, Tags, HyperLinks, ArticleFeedBack, PmUser, ArticleRelatedTags, \
    ArticleRelatedCategories, ArticleRequests


def get_article_data(article_id, request=None):
    """

    :param article_id:
    :param request:
    :return: returns the whole article data for the given article id, the request param is optional
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
    categories_list = ArticleRelatedCategories.objects.filter(articleId=each_article.id).values_list('category__name', flat=True)
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
        except Exception as e:
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


def article_review_check(*kwargs):
    for each_article in kwargs:
        article_request_status = get_article_request_status(each_article.get("articleData").id)
        if article_request_status == 'REQUESTED':
            each_article["isArticleRequested"] = True
    return kwargs


def get_article_request_status(article_id):
    try:
        article_request = ArticleRequests.objects.get(article=Article.objects.get(id=article_id))
        article_request_status = article_request.get_status()
    except:
        article_request_status = None
    return article_request_status


class ArticleManagement:
    def __init__(self):
        self.column_names = Article.get_model_field_names()
        self.insert_format = dict()

    def get_insert_format(self):
        for each_col in self.column_names:
            if each_col != "id":
                self.insert_format[each_col] = ""
        return self.insert_format

    def insert_article(self, data, additional_info=None):
        result_map = dict()
        additional_info_result = dict()
        additional_info_data = dict()
        try:
            result_obj = Article().create_article(data)
            if result_obj == "error":
                result_map["error"] = "something went wrong"
                return result_map
            else:
                if additional_info:
                    additional_info_result = self.add_related_article_data(additional_info)
                additional_info_data["articleId"] = result_obj.pk
                additional_info_data["tagsListIds"] = [each_tag_data.pk for each_tag_data in additional_info_result.get("tagsInfo") if additional_info_result.get("tagsInfo")]
                additional_info_data["categoryListIds"] = [each_category_data.pk for each_category_data in additional_info_result.get("categoryInfo") if additional_info_result.get("categoryInfo")]
                self.save_article_related_info(additional_info_data)
                result_map["success"] = result_obj
                return result_map
        except Exception as e:
            result_map["error"] = e.message
            return result_map

    def add_related_article_data(self, rel_modules):
        article_rel_data = {
            "tagsInfo": [],
            "categoryInfo": []
        }
        try:
            for module_key, module_value in rel_modules.iteritems():
                if module_key in ARTICLE_RELATED_MODULES:
                    for each_module in module_value:
                        if module_key == "tags":
                            tag_data = Tags().save_tag(each_module)
                            article_rel_data["tagsInfo"].append(tag_data)
                        if module_key == "categories":
                            category_data = Categories().save_category(each_module)
                            article_rel_data["categoryInfo"].append(category_data)
            return article_rel_data
        except Exception as e:
            article_rel_data["error"] = "something went wrong"
            return article_rel_data

    def save_article_related_info(self, article_rel_data):
        try:
            if article_rel_data.get("articleId"):
                for each_tag_id in article_rel_data.get("tagsListIds"):
                    ArticleRelatedTags().map_article_with_tags(article_rel_data.get("articleId"), each_tag_id)
                for each_category_id in article_rel_data.get("categoryListIds"):
                    ArticleRelatedCategories().map_article_with_category(article_rel_data.get("articleId"), each_category_id)
        except Exception as e:
            return "error while adding related info"






