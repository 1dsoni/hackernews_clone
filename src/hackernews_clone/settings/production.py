import os

SECRET_KEY = os.getenv('SECRET_KEY', 'random03l%&8d(%j)pu_pvy$@s!m1rm&6rq_^=ui!*c&7=e(9r4anf41')

DEBUG = False

ALLOWED_HOSTS = ['hnews_clone.herokuapp.com',]

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', ''),
    )
}

CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True
