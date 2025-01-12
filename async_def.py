from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}") # @app.get("/items/{item_id}") is a FastAPI route decorator that registers the function as a GET endpoint at /items/{item_id}
async def read_item(item_id: int): # read_item is an asynchronous function (async def) that takes a parameter item_id (type int) from the URL path
    return {"item_id": item_id} # When this endpoint is called, it returns a JSON response with the item_id

# Example Request:
# URL: /items/42
# Response: {"item_id": 42}

# Wrapper async function
async def main(): # main is an asynchronous function designed to call read_item and print its result
    result = await read_item(1) # Calls the read_item coroutine with item_id=1 # The await keyword suspends execution of main until read_item completes # Once completed, result is assigned the return value: {"item_id": 1}
    print(result) # print(result) outputs the result to the console

# Run the async function using asyncio
import asyncio
asyncio.run(main()) # asyncio.run(main()) starts an event loop and executes the main coroutine # It initializes the loop, runs main until it completes, and then cleans up the loop. # When main executes, the read_item coroutine is called, and its result is printed.

# Execution Flow:
# asyncio.run(main()) begins the execution of the main coroutine.
# Inside main:
 # read_item(1) is called, and FastAPI’s logic for the path operation runs.
 # The return value, {"item_id": 1}, is assigned to result.
 # The result is printed: {'item_id': 1}.

# Output:
# When this script runs:

 # The read_item function is called with item_id=1.
 # It returns {"item_id": 1}.
 # The main function prints the result: {'item_id': 1}

