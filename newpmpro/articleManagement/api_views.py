from rest_framework.response import Response
from rest_framework.views import APIView
from newpmpro.models import PmUser, ArticleFeedBack, Article


class VoteForTheArticle(APIView):
    def post(self, request):
        try:
            like_count = 0
            article_id = request.data.get("articleId")
            user_object = PmUser.objects.get(email=request.user.email)
            try:
                article_feedback_object = ArticleFeedBack.objects.get(article__id=article_id)
                if article_feedback_object.user is not user_object:
                    article_feedback_object.likeCount = like_count+1
                    article_feedback_object.save()
                    return Response({"result": "success", "message": "thanks for your feedback"}, 200)
                else:
                    return Response({"result": "error", "message":"you have already voted for this article"}, 500)
            except ArticleFeedBack.DoesNotExist:
                article_object = Article.objects.get(id=article_id)
                article_feedback_obj = ArticleFeedBack(article=article_object, user=user_object, likeCount=like_count+1)
                article_feedback_obj.save()
                return Response({"result": "success", "message": "thanks for your feedback"}, 200)
        except Exception as e:
            return Response({"result": "error", "message": "something went wrong. please try again later"}, 500000)