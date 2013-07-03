from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def get_param(request, name, default=None, strip=True):
    input_data = default
    if name in request.POST:
        input_data = request.POST[name]
    elif name in request.GET:
        input_data = request.GET[name]
    if input_data and strip:
        input_data = input_data.strip()
    return input_data


def is_blank(param):
    return param is None or param == ''


def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
