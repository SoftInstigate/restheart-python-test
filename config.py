# ------------------------------- #
# Global constants for REST calls #
# ------------------------------- #

__author__ = 'mturatti'

_BASE_URL = 'http://localhost:8080'
_DATABASE = '/mytestdb'
DATABASE_URL = _BASE_URL + _DATABASE
COLLECTION_URL = DATABASE_URL + "/testcollection"

HEADERS = {'Content-type': 'application/hal+json', 'Accept': '*/*'}
