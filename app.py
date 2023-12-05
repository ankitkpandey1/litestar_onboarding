from litestar import Litestar, get
from routers import future_router
from middlewares import RequestMiddleware

@get("/")
async def hello() -> str:
    return "Hello, world!"





app = Litestar(route_handlers=[hello, future_router], middleware=[RequestMiddleware])