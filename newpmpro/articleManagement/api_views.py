from rest_framework.response import Response
from rest_framework.views import APIView
from articleManagement.models import PmUser, ArticleFeedBack, Article


class VoteForTheArticle(APIView):
    def post(self, request):
        try:
            like_count = 0
            users_objects_list = list()
            article_id = request.data.get("articleId")
            user_object = PmUser.objects.get(email=request.user.email)
            try:
                article_feedback_object_list = ArticleFeedBack.objects.filter(article__id=article_id)
                for each_user_obj in article_feedback_object_list:
                    users_objects_list.append(each_user_obj.user)
                if user_object not in users_objects_list:
                    article_object = Article.objects.get(id=article_id)
                    article_feedback_obj = ArticleFeedBack(article=article_object, user=user_object, likeCount=like_count+1)
                    article_feedback_obj.save()
                    return Response({"result": "success", "message": "thanks for your feedback"}, 200)
                else:
                    return Response({"result": "error", "message": "you have already voted for this article"}, 500)
            except ArticleFeedBack.DoesNotExist:
                article_object = Article.objects.get(id=article_id)
                article_feedback_obj = ArticleFeedBack(article=article_object, user=user_object, likeCount=like_count+1)
                article_feedback_obj.save()
                return Response({"result": "success", "message": "thanks for your feedback"}, 200)
        except Exception as e:
            return Response({"result": "error", "message": ""}, 500)


class SendArticleForReview(APIView):
    def post(self, request):
        try:
            return Response({"result": "success"}, 200)
        except Exception as e:
            return Response({"result": "error", "message": "something went wrong. please try again later"}, 500)
