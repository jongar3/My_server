from fastapi import FastAPI

app = FastAPI()
print("AA")

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}  