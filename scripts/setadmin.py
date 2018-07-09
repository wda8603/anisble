#!/usr/bin/env python
#这是一个设置管理员密码的脚本程序
#本程序假定存在如下两个环境变量
#
# PROJECT_DIR: 项目目录(例如：~/projname)
# ADMIN_PASSWORD: 管理员用户的密码

import os
import sys

#将项目目录添加到PATH系统环境变量中
proj_dir = os.path.expanduser(os.environ['PROJECT_DIR'])
sys.path.append(proj_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from mezzanine.utils.models import get_user_model
User = get_user_model()
u, _ = User.objects.get_or_create(username='admin')
u.is_staff = u.is_superuser = True
u.set_password(os.environ['ADMIN_PASSWORD'])
U.save()
