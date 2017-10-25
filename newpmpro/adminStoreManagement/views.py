from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from rest_framework.response import Response
from adminStoreManagement.utils import get_defaults_for_dashboard
from newpmpro.exceptions import UnAuthorizedException


@never_cache
@user_passes_test(lambda u: u.is_superuser, login_url='/store/adminlogin')
def get_dashboard_page(request):
    context = {
        "statistics": get_defaults_for_dashboard()
    }
    return render(request, 'adminStoreManagement/adminAction.html', context)


@never_cache
def get_admin_login_page(request):
    return render(request, 'adminStoreManagement/adminHome.html')


@never_cache
@require_http_methods(['POST'])
def login_as_admin(request):
    try:
        email = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password, type='superuser')
        if user is None or not user.is_staff:
            raise UnAuthorizedException("you are not authorized to perform this action")
        login(request, user)
        return JsonResponse({"success": "successfully logged in"}, status=200)
    except MultiValueDictKeyError as e:
        # logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
        return JsonResponse({"error": "Invalid username or password"}, status=500)
    except UnAuthorizedException as e:
        # logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
        return JsonResponse({"error": "you are not authorized to perform this action"}, status=403)
    except Exception as e:
        # logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
        return JsonResponse({"error": str(e)}, status=500)
