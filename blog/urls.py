# coding=UTF-8

from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^index/$', views.index),  # 斜杠不能少
]
