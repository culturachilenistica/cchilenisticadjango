#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$',views.inicio),
    url(r'^juego.html$',views.empezar_juego),
]