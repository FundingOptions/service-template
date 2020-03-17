from fastapi import APIRouter, Depends, FastAPI
from fastapi.security import APIKeyHeader


class router:
    public = APIRouter()
    private = APIRouter()


@router.public.get("/hello/{name}")
def hello(name: str = "World") -> str:
    return f"Hello, {name}!"


app = FastAPI()
app.include_router(router.public)
app.include_router(
    router.private,
    dependencies=[Depends(APIKeyHeader(name="x-api-key", auto_error=False))],
)
