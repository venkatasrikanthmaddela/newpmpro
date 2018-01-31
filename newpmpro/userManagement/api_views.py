from _mysql_exceptions import IntegrityError
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from logger import logger
from django.contrib.auth import authenticate, login, logout, get_user_model
import datetime

from newpmpro.exceptions import UnAuthorizedException
from newpmpro.models import UserSources
from newpmpro.settings import ADMIN_LOGIN_URL
from newpmpro.utils import get_log_string, get_friendly_name
from django.utils.datastructures import MultiValueDictKeyError


class LoginUser(APIView):
    def post(self, request):
        USERMODEL = get_user_model()
        try:
            user = USERMODEL.objects.get(email=request.data["email"])
            if user:
                user_sources = UserSources.objects.filter(user=user).values_list('sources', flat=True)
                if 'google' in user_sources or 'facebook' in user_sources:
                    return Response({"error": "Please log in with " + ' or '.join(user.sources)}, 500)
                user = authenticate(email=request.data["email"], password=request.data["password"], type='user')
                if user is None:
                    raise UnAuthorizedException("Invalid User Name or Password")
                login(request, user)
                return Response({
                    "result": user.username,
                    "email": user.email,
                    "name": user.username,
                    "mobile": user.mobileNumber,
                    "success": True
                }, 200)
        except USERMODEL.DoesNotExist:
            return Response({"error": "Invalid username or password"}, 500)
        except MultiValueDictKeyError as e:
            # logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
            return Response({"error": "Invalid username or password"}, 500)
        except UnAuthorizedException as e:
            # logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
            return Response({"error": e.message}, 401)
        except Exception as e:
            # logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
            return Response({"error": str(e)}, 500)

    def get(self, request):
        return Response({"success":"result"}, 500)


class SignUpUser(APIView):
    def post(self, request, source):
        try:
            if source == 'direct':
                return sign_up_directly(request)
        except:
            return Response({"result": "error"}, 500)
        return Response({"result": "success"}, 200)


class LogoutUser(APIView):
    def get(self, request):
        try:
            logout(request)
            if request.path == ADMIN_LOGIN_URL:
                return redirect(ADMIN_LOGIN_URL)
            else:
                return redirect('/')
        except Exception as e:
            logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
            return Response({"result": "error"}, 500)


class LogoutAdmin(APIView):
    def get(self, request):
        try:
            logout(request)
            return redirect(ADMIN_LOGIN_URL)
        except Exception as e:
            logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
            return Response({"result": "error"}, 500)


class CheckUserLogin(APIView):
    def get(self, request):
        try:
            email = request.user.email
            return Response({"success": email}, 200)
        except:
            return Response({"error": "user is not logged in"}, 500)


def create_user(name, email, phone, password, source, is_staff=False, is_subscribed=False):
    USERMODEL = get_user_model()
    try:
        user = USERMODEL.objects.get(email=email)
    except USERMODEL.DoesNotExist:
        user = None
    try:
        if user:
            all_sources = UserSources.objects.filter(user=user).values_list('sources', flat=True)
            if source not in all_sources:
                source_obj = UserSources(user=user, sources=source)
                source_obj.save()
            return False, {"message": 'user already exists'}
        else:
            user = USERMODEL.objects.create_user(name, email, password, phone, is_staff, is_subscribed)
            source_object = UserSources(user=user, sources=source)
            source_object.save()
            return True, {"name": user.username, "email": user.email, "password":password}
    except IntegrityError as e:
        return False, {"message": 'user already exists'}
    except Exception as e:
        logger.error(get_log_string('error: '+str(e)), exc_info=True)
        return False, {"message": str(e)}


def sign_up_directly(request):
    try:
        success, data = create_user(request.data['name'], request.data['email'], request.data['phoneNumber'], request.data['password'], 'direct', False, request.data.get("isSubscribed", False))
        if success:
            user = authenticate(email=data.get("email"), password=data.get("password"), type='user')
            login(request, user)
            return Response({"name":data.get("name"), "email":data.get("email")}, 200)
        else:
            return Response({"error": data['message']}, 500)
    except MultiValueDictKeyError as e:
        logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
        return Response({"error": get_friendly_name(str(e))+' is missing from the input data'}, 500)
    except Exception as e:
        logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
        return Response({"error": str(e)}, 500)