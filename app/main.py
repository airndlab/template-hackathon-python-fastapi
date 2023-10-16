from fastapi import FastAPI

from app import logic

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "UP"}


# TODO: Remove
@app.get("/logic")
async def root():
    result = logic.do_logic()
    return {"result": result}
