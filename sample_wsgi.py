import os
import sys

path = '/home/nirpa/hamronepal'

if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODUEL'] = 'hamronepal.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())