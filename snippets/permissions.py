#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 14:10
# @Author : "wuyang"
# @Email : wuyang_229@126.com
# @File : permissions.py
# @Software: PyCharm

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user