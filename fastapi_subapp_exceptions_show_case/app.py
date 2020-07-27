from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.get("/app")
def read_main():
    raise UnicornException(name="main")


foo = FastAPI()


@foo.get("/foo")
async def read_foo():
    raise UnicornException(name="foo")


app.mount("/foo", foo)


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(status_code=418, content={"message": f"Oops! {exc.name}"},)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
