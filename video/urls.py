from django.conf.urls import include
from django.urls import re_path
from . import views
from video.views import showvideo, hello, addlike, oneVideo, addcomment

urlpatterns = [
    re_path(r'^$', showvideo),
    re_path(r'get/(?P<video_id>\d+)/$', oneVideo),
    re_path(r'^addlikes/(?P<video_id>\d+)/$', addlike),
    re_path(r'^video/addcomment/(?P<video_id>\d+)/$', addcomment)
]
