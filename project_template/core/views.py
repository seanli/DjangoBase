from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from core.decorators import ajax_endpoint
from core.models import User
from core.utils.client import get_param, is_blank, is_valid_email
from core.utils.auth import user_login


def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@ajax_endpoint
def api_user_add(request):
    response = {}
    email = get_param(request, 'email')
    password = get_param(request, 'password', strip=False)
    password_conf = get_param(request, 'password_conf', strip=False)
    errors = {}
    if is_blank(email):
        errors['email'] = 'Sorry! You need an e-mail address to sign up.'
    elif not is_valid_email(email):
        errors['email'] = 'Sorry! Please put a valid e-mail address.'
    if is_blank(password):
        errors['password'] = 'Sorry! You need a password to sign up.'
    if is_blank(password_conf):
        errors['password_conf'] = 'Please confirm your password.'
    elif password != password_conf:
        errors['password_conf'] = 'Oops! Your passwords do not match.'
    try:
        User.objects.get(email=email)
        errors['email'] = 'Sorry! This e-mail address is being used.'
    except User.DoesNotExist:
        pass
    if len(errors.keys()) > 0:
        response['errors'] = errors
        return response, 200
    new_user = User(email=email)
    new_user.set_password(password)
    new_user.save()
    response['user'] = new_user.id
    user_login(request, new_user)
    return response, 201


@ajax_endpoint
def api_user_login(request):
    response = {}
    email = get_param(request, 'email')
    password = get_param(request, 'password', strip=False)
    errors = {}
    if is_blank(email):
        errors['email'] = 'Sorry! You need an e-mail address to login.'
    if is_blank(password):
        errors['password'] = 'Sorry! You need a password to login.'
    if not (is_blank(email) or is_blank(password)):
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                errors['__all__'] = 'Sorry! This account is inactive.'
        else:
            errors['__all__'] = 'Sorry! Your credentials are incorrect.'
    if len(errors.keys()) > 0:
        response['errors'] = errors
        return response, 200
    return response, 200
