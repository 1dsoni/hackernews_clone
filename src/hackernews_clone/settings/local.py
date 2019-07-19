from .base import *

import os
SECRET_KEY = 's03^od9g(2cy&kibe5p3no%vlbr0r1#yk^kb@*i3z_2h*sb^md'

DEBUG = True

ALLOWED_HOSTS = [ 'hnewsclone.herokuapp.com',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
