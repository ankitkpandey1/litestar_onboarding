from typing import Annotated
from litestar import get, Controller

from litestar.openapi.spec.example import Example
from litestar.params import Parameter, Body

future_maps = {
    1: "future1",
    2: "future2",
    3: "future3",
    4: "future4",
}


class FutureController(Controller):
    @get(path="/{future_id:int}")
    async def get_future_id_status(
        self,
        future_id: Annotated[
            int,
            Parameter(
                description="The ID of the future to retrieve",
                ge=0,
            ),
        ],
    ) -> str:
        return "tt"
