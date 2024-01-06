import pytest
import os

@pytest.fixture
def setup_default_environment_vars():
    os.environ['SYSTEM'] = 'default_system'
    os.environ['APPLICATION'] = 'default_application'
    os.environ['DEPLOYABLE_UNIT'] = 'default_unit'
    os.environ['SERVICE_VERSION'] = '1.0'
    from extensions.configuration import set_defaults, service_namespace, service_name
    return set_defaults, service_namespace, service_name


def test_set_service_namespace_and_name_with_environment_vars(setup_default_environment_vars):
    set_defaults, service_namespace, service_name = setup_default_environment_vars

    assert service_namespace() == 'default_system.default_application'
    assert service_name() == 'default_system.default_application.default_unit'