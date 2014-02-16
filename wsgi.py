"""
WSGI config for quirktonomicon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys, site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/aaron/quirktonomicon/quirkenv/local/lib/python2.7/site-packages')

sys.path.append('/home/aaron/quirktonomicon')
sys.path.append('/home/aaron/quirktonomicon/quirktonomicon')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quirktonomicon.settings")

# Activate your virtual env
activate_env="/home/aaron/quirktonomicon/quirkenv/bin/activate_this.py"
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
