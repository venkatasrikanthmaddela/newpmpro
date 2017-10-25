from django.conf.urls import url
from adminStoreManagement.views import get_dashboard_page, login_as_admin, get_admin_login_page

urlpatterns = [
    url('adminlogin', get_admin_login_page),
    url('', get_dashboard_page, name='admin-login-page')
]
