from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from core.schemas.schema import Ans, Item

from v1.status import router

app = FastAPI()

app.include_router(router)

# In-memory storage of to-do items
to_do_list: List[Item] = []


# @app.get("/todos/", response_model=Ans)
# async def read_todos():
#     a = [i for i in range(1000)]
#     k = Ans(name="Helo", completed=True, l=a)
#     return k


# @app.post("/todos/", response_model=Item)
# async def create_todo(item: Item):
#     to_do_list.append(item)
#     return item


# @app.put("/todos/{item_id}", response_model=Item)
# async def update_todo(item_id: int, item: Item):
#     if item_id >= len(to_do_list):
#         raise HTTPException(status_code=404, detail="Item not found")
#     to_do_list[item_id] = item
#     return item


# @app.delete("/todos/{item_id}")
# async def delete_todo(item_id: int):
#     if item_id >= len(to_do_list):
#         raise HTTPException(status_code=404, detail="Item not found")
#     to_do_list.pop(item_id)
#     return {"detail": "Item deleted"}
