from django.urls import re_path
from . import views
from galery.views import showimg

urlpatterns = [
    re_path(r'^', showimg),
    ]