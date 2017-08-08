from django.conf.urls import url

from searchProjectManagement.api_views import RequestForProject

urlpatterns = [
    url('request-for-project', RequestForProject.as_view()),
]