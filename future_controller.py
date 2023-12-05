from litestar import get, Controller

future_maps = {
    1: "future1",
    2: "future2",
    3: "future3",
    4: "future4",
}

class FutureController(Controller):

    @get(path="/{future_id:int}")
    async def get_future_id_status(self, future_id: int):
        ...
 