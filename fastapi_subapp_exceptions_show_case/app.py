from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.get("/app")
def read_main():
    raise UnicornException(name="MAIN")


foo = FastAPI()

@foo.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}

app.mount("/foo", foo)

bar = FastAPI()

@bar.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/bar", bar)

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)