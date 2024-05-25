from .service import (
    set_defaults,
    service_namespace,
    service_name,
    service_version,
    hostname,
    process_id,
    service_instance,
    environment
)

from .config import (
    make_dataclass_from_config,
    read_configs,
    read_configs_to_dataclass
)
