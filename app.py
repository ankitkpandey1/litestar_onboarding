from litestar import Litestar, get
from routers import future_router

@get("/ping")
async def hello() -> str:
    return "pong!"





app = Litestar(route_handlers=[hello, future_router])