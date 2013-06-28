from django.conf.urls import patterns, url


urlpatterns = patterns('core.views',
    url(r'^$', 'index'),
    url(r'^logout/$', 'logout'),
    url(r'^api/user/add/$', 'api_user_add'),
    url(r'^api/user/login/$', 'api_user_login'),
)
