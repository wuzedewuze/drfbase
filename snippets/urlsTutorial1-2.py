#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 11:31
# @Author : "wuyang"
# @Email : wuyang_229@126.com
# @File : urls.py
# @Software: PyCharm


from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)