import os
import platform
import uuid

from .hosting_environment import _environment

_system = os.environ.get('SYSTEM')
_application = os.environ.get('APPLICATION')
_deployable_unit = os.environ.get('DEPLOYABLE_UNIT')

_hostname = platform.node()
_instance = str(uuid.uuid4())
_process_id = os.getpid()

_service_version = os.environ.get('SERVICE_VERSION')


def environment():
    return _environment
def hostname():
    return _hostname

def service_instance():
    return _instance

def process_id():
    return _process_id
def service_namespace():
    return f'{_system}.{_application}'

def service_name():
    return f'{service_namespace()}.{_deployable_unit}'

def service_version():
    return _service_version

def set_defaults(
        system=None,
        application=None,
        deployable_unit=None,
        version=None
):
    global _system, _application, _deployable_unit, _service_version

    if system is not None:
        _system = system

    if application is not None:
        _application = application

    if deployable_unit is not None:
        _deployable_unit = deployable_unit

    if version is not None:
        _service_version = version