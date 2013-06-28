from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)


@ajax_endpoint
def test_endpoint(request):
    response = {}
    if request.user.is_authenticated():
        response['user'] = request.user.email
    return response, 200
