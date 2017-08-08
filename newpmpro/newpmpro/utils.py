from django.core.exceptions import ImproperlyConfigured



FRIENDLY_NAMES = {
    'email': 'Email Id',
    'phoneNumber': 'Phone Number',
    'password': 'Password'
}



# def get_user_model():
#     "Return the User model that is active in this project"
#     from django.conf import settings
#     from django.db.models import get_model
#
#     try:
#         app_label, model_name = settings.AUTH_USER_MODEL.split('.')
#     except ValueError:
#         raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.model_name'")
#     user_model = get_model(app_label, model_name)
#     if user_model is None:
#         raise ImproperlyConfigured("AUTH_USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL)
#     return user_model


def get_log_string(message, request=None):
    log = message
    if request:
        user_status = ''
        if request.user.is_authenticated():
            user_status = 'User: ' + request.user.id
        log = "{0} || Session: {1} || Path: {2} || {3}".format(user_status, get_session_key(request), request.path,
                                                               message)
    return log


def get_session_key(request):
    return request.session._session_key


def get_friendly_name(key):
    return FRIENDLY_NAMES.get(key, key)