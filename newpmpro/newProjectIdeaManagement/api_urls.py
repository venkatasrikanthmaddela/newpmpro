from django.conf.urls import url

from newProjectIdeaManagement.api_views import SaveProjectIdea

urlpatterns = [
    url('send-project-idea', SaveProjectIdea.as_view())
]