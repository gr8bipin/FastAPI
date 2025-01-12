# async def syntax for path operation functions
# background about asynchronous code, concurrency and parallelism

# If you are using third party libraries that tell you to call them with await, like:
results = await some_library()

# Then, declare your path operation functions with async def like:
@app.get('/')
async def read_results():
    results = await some_library()
    return results
# Note: You can only use await inside of functions created with async def.

# If you are using a third party library that communicates with something (a database, an API, the file system, etc.)
# and doesn't have support for using await, (this is currently the case for most database libraries), then declare 
# your path operation functions as normally, with just def, like:
@app.get('/')
def results():
    results = some_library()
    return results
# If your application (somehow) doesn't have to communicate with anything else and wait for it to respond, use async def.
# If you just don't know, use normal def.