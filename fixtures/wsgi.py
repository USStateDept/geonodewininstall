#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geonode.settings")




import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('__geonodedir__/venv/Lib/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('__geonodedir__/GeoNode')
sys.path.append('__geonodedir__/Geonode/geonode')


# Activate your virtual env
activate_env=os.path.expanduser("__geonodedir__/venv/Scripts/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()