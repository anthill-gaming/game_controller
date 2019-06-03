from anthill.platform.services import PlainService, ControllerRole
from anthill.platform.api.internal import as_internal
from psutil import virtual_memory, cpu_percent


class Service(ControllerRole, PlainService):
    """Anthill default service."""
    master = 'game_master'

    @staticmethod
    def setup_internal_api():
        @as_internal()
        async def heartbeat_report(api, **options):
            return {
                'memory': virtual_memory().percent,
                'cpu': cpu_percent()
            }
