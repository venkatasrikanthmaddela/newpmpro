from django.conf.urls import url
from adminStoreManagement.views import get_dashboard_page, login_as_admin, get_admin_login_page, get_requests

urlpatterns = [
    url(r'^$', get_dashboard_page, name='admin-login-page'),
    url(r'see-project-requests/$', get_requests),
    url(r'adminlogin/$', get_admin_login_page),
]
