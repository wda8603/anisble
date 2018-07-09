#!/usr/bin/env python
#这是一个设置王者域名的脚本程序
#本程序假定存在如下两个环节变量
#
#PROJECT_DIR: 项目目录(例如：~/projname)
#WEBSITE_DOMAIN: 网站的域名 (例如：www.example.com)

import os
import sys

#将项目目录添加到PATH系统环境变量中
proj_dir = os.path.expanduser(os.environ['PROJECT_DIR']
Sys.path.append(proj_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.conf import settings
from django.contrib.sites.models import Site

domain = os.environ['WEBSITE_DOMAIN']
Site.objects.filter(id=settings.SITE_ID).update(domain=domain)
Site.objects.get_or_create(domain=domain)



