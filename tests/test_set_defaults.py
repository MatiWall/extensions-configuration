import pytest

# Assuming your module is named 'your_module', replace it with the actual module name.

@pytest.fixture
def setup_defaults():
    from extensions.configuration import set_defaults, service_namespace, service_name
    # This fixture sets up the default values before each test.
    set_defaults(system='default_system', application='default_application', deployable_unit='default_unit',
                 version='1.0')
    return set_defaults, service_namespace, service_name


def test_set_defaults_with_values(setup_defaults):
    set_defaults, service_namespace, service_name = setup_defaults
    # Test set_defaults with specific values
    set_defaults(system='new_system', application='new_application', deployable_unit='new_unit', version='2.0')

    assert service_namespace() == 'new_system.new_application'
    assert service_name() == 'new_system.new_application.new_unit'


def test_set_defaults_with_defaults(setup_defaults):
    set_defaults, service_namespace, service_name = setup_defaults

    set_defaults()

    assert service_namespace() == 'default_system.default_application'
    assert service_name() == 'default_system.default_application.default_unit'


def test_set_defaults_with_partial_values(setup_defaults):
    set_defaults, service_namespace, service_name = setup_defaults
    set_defaults(application='partial_application', version='3.0')

    assert service_namespace() == 'default_system.partial_application'
    assert service_name() == 'default_system.partial_application.default_unit'




