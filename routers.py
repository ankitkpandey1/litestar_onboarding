from litestar import Litestar, get, Controller, Router
from future_controller import FutureController

future_router = Router(path="/future", route_handlers=[FutureController])