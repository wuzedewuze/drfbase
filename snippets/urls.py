#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 15:13
# @Author : "wuyang"
# @Email : wuyang_229@126.com
# @File : urls.py
# @Software: PyCharm

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]