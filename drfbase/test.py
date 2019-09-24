#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 11:38
# @Author : "wuyang"
# @Email : wuyang_229@126.com
# @File : test.py
# @Software: 全局测试，可以直接创建modle实例入库等操作

import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'drfbase.settings'
django.setup()


if __name__ == '__main__':

    from snippets.models import Snippet
    snip = Snippet()
    print(snip)