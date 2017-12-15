from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/posts/$', views.post_list_set),
    url(r'^api/post/(?P<pk>\d+)$', views.post_detail_view),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/change/$', views.post_change, name='post_change'),
    url(r'^api/message/$', views.message),
]
urlpatterns = format_suffix_patterns(urlpatterns)