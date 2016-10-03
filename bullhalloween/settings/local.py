#! /usr/bin/env python2.7
from default import *

"""
This is the local settings template file. So, do not modify this file.
Instead, make a copy as "local.py" and set the development variables in it.
"""

# local settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = True


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite')
}


if DEBUG:
    # set INTERNAL_IPS to entire local network
    from fnmatch import fnmatch

    class WildcardNetwork(list):
        def __contains__(self, key):
            for address in self:
                if fnmatch(key, address):
                    return True
            return False

    INTERNAL_IPS = WildcardNetwork(['127.0.0.1', '192.168.*.*'])

    # URL that handles the media, static, etc.
    STATIC_URL = '/static/'
    MEDIA_URL = STATIC_URL + 'media/'

    INSTALLED_APPS += (
        # 'debug_toolbar',
    )
