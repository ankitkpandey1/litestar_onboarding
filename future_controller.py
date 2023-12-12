from typing import Optional
from litestar import get, Controller, post, Response, patch
from litestar.di import Provide
from pydantic import BaseModel, Field
future_maps = {
    1: "future1",
    2: "future2",
    3: "future3",
    4: "future4",
   
}


class FutureRequestCreate(BaseModel):
    future_id: Optional[int] = Field(
        description="Future ID",
        examples=[1],
    )
    future_name: str
    additional_info: Optional[dict] = Field(
        description="Random additional info",
        default=None,  # for making it optional
    )
    
    
class FutureRequestPatch(BaseModel):
    ...

class FutureController(Controller):

    @get(path="/{future_id:int}")
    async def get_future_id_status(self, future_id: int) -> str:
        return future_maps.get(future_id)
 
    @post(path="/")
    async def create_future(self, data: FutureRequestCreate) -> str:
        future_maps[data.future_id] = data.future_name
        return future_maps.get(data.future_id)
    
    
    @patch(path="/{future_id:int}")
    async def update_future(self, future_id: int, data: FutureRequestPatch) -> str:
        return "future updated"