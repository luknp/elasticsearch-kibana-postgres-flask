import os
import urllib

POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = urllib.parse.quote_plus(str(os.environ.get('POSTGRES_PORT', '15432')))
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'thegames')
POSTGRES_USER = urllib.parse.quote_plus(str(os.environ.get('POSTGRES_USER', 'root')))
POSTGRES_PASSWORD = urllib.parse.quote_plus(str(os.environ.get('POSTGRES_PASSWORD', 'password')))


DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode=prefer'.format(POSTGRES_USER,POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB)
ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL', 'http://elastic:changeme@localhost:9200')

