from anthill.framework.utils.asynchronous import as_future


class SpawnError(Exception):
    pass


class Room:
    pass


class GameServer:
    async def spawn(self):
        pass

    async def terminate(self):
        pass
