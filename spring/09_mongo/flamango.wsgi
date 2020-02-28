#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/flamango/")
sys.path.insert(0,"/var/www/flamango/flamango/")

import logging
logging.basicConfig(stream=sys.stderr)

from flamango import app as application