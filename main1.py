from typing import List

from fastapi import FastAPI,  HTTPException
from models1 import Todo, Todo_Pydantic, TodoIn_Pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from pydantic import BaseModel

from pydantic_models import User

# Define a simple message model for responses
class Message(BaseModel):
    message: str

# Initialize FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# Create a Todo item
@app.post("/todo", response_model=Todo_Pydantic)
async def create(todo: TodoIn_Pydantic): # type: ignore
    obj = await Todo.create(**Todo.dict(exclude_unset=True))
    return await Todo_Pydantic.from_tortoise_orm(obj)

# Retrieve a Todo item by ID
@app.get("/todo/{id}", response_model=Todo_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_one(id: int):
    return await Todo_Pydantic.from_queryset_single(Todo.get(id=id))

# Update a Todo item
@app.put("/todo/{id}", response_model=Todo_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update(id:id, todo: TodoIn_Pydantic):  # type: ignore
    # Check if the Todo item exists
    await Todo.get(id = id) # Raises a 404 if not found
    # Update the Todo item
    await Todo.filter(id=id).update(**Todo.dict(exclude_unset=True))
    # Return the updated Todo item
    return await Todo_Pydantic.from_queryset_single(Todo.get(id=id))

# Delete a Todo item
@app.delete("/todo/{id}", response_model=Message, responses={404: {"model": HTTPNotFoundError}})
async def delete(id: int):
    delete_obj = await Todo.filter(id=id).delete()
    if not delete_obj:
        raise HTTPException(status_code=404, detail="This todo is not found.")
    return Message(message="Succesfully Deleted")

# Register Tortoise ORM
register_tortoise(
    app,
    db_url="sqlite://store.db",
    modules={'models': ['models1']},
    generate_schemas=True,
    add_exception_handlers=True
)