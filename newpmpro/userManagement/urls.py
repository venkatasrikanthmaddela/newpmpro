from django.conf.urls import url, include
from userManagement.views import DashBoardPage

urlpatterns = [
   url('dashboard', DashBoardPage.as_view(), name="dash-board")
]