# -*- coding: utf-8 -*-

import sys
import site

sys.path.insert(0, '/var/www/misc/myip')
site.addsitedir('/usr/lib/python-env/lib/python2.6/site-packages')

from main import app as application
