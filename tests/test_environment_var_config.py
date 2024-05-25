# import pytest
# import os
#
# @pytest.fixture
# def setup_default_environment_vars():
#     os.environ['SYSTEM'] = 'default_system'
#     os.environ['APPLICATION'] = 'default_application'
#     os.environ['DEPLOYABLE_UNIT'] = 'default_unit'
#     os.environ['SERVICE_VERSION'] = '1.0'
#     return
#
#
# def test_set_service_namespace_and_name_with_environment_vars(setup_default_environment_vars):
#     from extensions.configuration import set_defaults, service_namespace, service_name
#
#     assert service_namespace() == 'default_system.default_application'
#     assert service_name() == 'default_system.default_application.default_unit'