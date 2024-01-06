import os

_HOSTING_ENVIRONMENT = 'ENVIRONMENT'

PRODUCTION = 'Production'
DEVELOPMENT = 'Development'

_environment = os.environ.get(_HOSTING_ENVIRONMENT, DEVELOPMENT)

def is_production():

    return _environment == PRODUCTION
