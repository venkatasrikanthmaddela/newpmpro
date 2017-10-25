from django.conf.urls import url

from userManagement.api_views import LoginUser, LogoutUser, SignUpUser, CheckUserLogin, LogoutAdmin

urlpatterns = [
    url('login', LoginUser.as_view()),
    url('logout', LogoutUser.as_view(), name='log-out'),
    url('admin-log-out', LogoutAdmin.as_view(), name='admin-log-out'),
    url('signup/(\w+)', SignUpUser.as_view()),
    url('is-user-logged-in', CheckUserLogin.as_view()),
]