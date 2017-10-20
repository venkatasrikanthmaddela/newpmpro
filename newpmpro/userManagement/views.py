from django.shortcuts import render
from django.views import View
from articleManagement.models import ArticleRequests
from newpmpro.models import PmUser


class DashBoardPage(View):
    def get(self, request):
        dashboard_data = dict()
        if request.GET.get("page") == "article-requests":
            user_article_requests = ArticleRequests.objects.filter(user=PmUser.objects.get(email=request.user.email))
            dashboard_data["articleRequests"] = user_article_requests
        return render(request, 'userManagement/dashboard.html', {"dashBoardData": dashboard_data})