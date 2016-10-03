import os
import sys
import dj_database_url

DATABASES['default'] =  dj_database_url.config()


