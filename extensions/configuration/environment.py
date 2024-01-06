import os

_HOSTING_ENVIRONMENT = 'ENVIRONMENT'

PRODUCTION = 'Production'
DEVELOPMENT = 'Development'

environment = os.environ.get(_HOSTING_ENVIRONMENT, DEVELOPMENT)

def is_production():

    return environment == PRODUCTION
