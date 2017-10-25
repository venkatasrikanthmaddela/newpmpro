from django.conf.urls import url
from adminStoreManagement.views import login_as_admin

urlpatterns = [
    url('admin-login', login_as_admin),
]