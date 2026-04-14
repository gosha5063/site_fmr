from .base import *

DEBUG = False

# Serve static files from a directory that nginx (www-data) can read.
# Keeping it out of /home avoids common 403 permission issues.
STATIC_ROOT = Path(os.getenv('STATIC_ROOT', '/var/www/axelot/static'))

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
