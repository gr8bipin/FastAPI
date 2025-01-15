#The provided code implements a REST API using FastAPI, which is designed to manage a simple "To-Do" list.
##This code is a RESTFul API built using the FastAPI framework. It allows users to manage a simple To-Do List by performing CRUD operations: Create, Read, Update, and Delete.

#Imports
from fastapi import FastAPI, HTTPException #The framework used to create the API. #Used to raise HTTP errors, such as when an item s not found, it raises a 404 error.
from pydantic import BaseModel #A Pydantic model to validate and define the data structure for the Todo class or structure input data.
from typing import Optional, List #Typing utilities to define optional fields and list structures in the API(lists for data type annotations).

#Data Model
#This means that all input data is validated according to this structure.
class Todo(BaseModel): # Defines a Todo class to structure the data.
    name: str #The name of the task.
    due_date: str #The due date for the task as a string (e.g., "YYYY-MM-DD").
    description: str #A description of the task.

#API Initialization
app = FastAPI(title="Todo API") #Instantiates a FastAPI application with the title "Todo API."

# Create, Read, Update, Delete

#In-memory Data Storage
#An empty list (store_todo) acts as the database for storing To-Do items
store_todo = [] #A list (store_todo) is used to store the Todo items in memory. Since this is an in-memory store, the data will be lost when the server restarts.

#API Endpoints:
#GET /
#A simple root endpoint that returns a JSON response {"Hello": "World"}.
##Useful for Checking if the server or API is running:
@app.get("/")
async def home():
    return {"Hello": "World"}

#GET /today/
#Create a new Todo.
@app.post("/today/")
async def create_todo(todo: Todo): #Accepts a Todo object as input
    store_todo.append(todo) #appends Todo object to store_todo list.
    return todo #Returns the newly created Todo.

##Retrieve all Todos.
@app.get("/todo", response_model = List[Todo]) #Fetches and returns all To-Do items as a list of Todo objects.
async def get_all_todos():
    return store_todo

#Fetches a specific Todo by its index (id) in store_todo.
#If the index is invalid or out of range, a 404 error is raised with the message "Todo Not Found."
##Retrieve a specific Todo by its ID.
@app.get("/todo/{id}")
async def get_todo(id: int): 
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")

#Updates an existing Todo by its index (id) with the new Todo data provided.
#If the index is invalid, a 404 error is raised with the message "Todo Not Found."
##Update a Todo by its ID.
@app.put("/todo/{id}") #The {id} parameter is extracted from the URL.
async def update_todo(id: int, todo: Todo): #Updates an existing Todo by its index (id).
    try:
        store_todo[id] = todo #Attempts to retrieve the Todo at the given index in store_todo.
        return store_todo[id]
    except:
        raise HTTPException(status_code = 404, detail = "Todo Not Found") #If the index is invalid, raises a 404 error with the message "Todo Not Found."

# Deletes a Todo by its index (id) in store_todo.
# Returns the deleted Todo object.
# If the index is invalid, a 404 error is raised with the message "Todo Not Found."
##Delete a Todo by its ID.   
@app.delete("/todo/{id}") #The {id} parameter is extracted from the URL.
async def delete_todo(id: int): #Deletes a Todo by its index (id).

    try:
        obj = store_todo[id]
        store_todo.pop(id) #The Todo at the given index is removed using pop().
        return obj #Returns the deleted Todo.
    except:
        raise HTTPException(status_code = 404, detail = "Todo Not Found") #If the index is invalid, raises a 4/04 error.

#Key Features-
#Validation: The Todo model ensures that input data matches the required structure.
#Error Handling: Uses HTTPException to handle invalid operations (e.g., accessing an out-of-range index).
#CRUD Operations:
    #Create: POST /today/
    #Read: GET /todo and GET /todo/{id}
    #Update: PUT /todo/{id}
    #Delete: DELETE /todo/{id}

#This API is simple but provides a strong foundation for understanding RESTful services with FastAPI.