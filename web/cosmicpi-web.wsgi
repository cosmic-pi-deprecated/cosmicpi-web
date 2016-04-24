import logging, sys
logging.basicConfig(stream=sys.stderr)

from webserver import app as application