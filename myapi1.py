# Importing Required Modules:
    # FastAPI: Used to create and manage the API application.
    # Pydantic.BaseModel: A base class for creating models to validate and manage data inputs.
        # With BaseModel, FastAPI can validate incoming JSON requests and ensure the data conforms to the model's structure and types.
from fastapi import FastAPI
from pydantic import BaseModel

# Initializing the FastAPI App:
    # Initializes the application instance named app, which serves as the entry point for defining API routes.
app = FastAPI()

# The Item class inherits from Pydantic.BaseModel and defines the structure for input data.
# Defining a Pydantic Model:
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True # A boolean indicating whether the item is in stock. If not provided, it defaults to True.

    # Key Notes:
        # FastAPI ensures the data sent to the API matches the structure defined in the Item model. If the data is invalid, FastAPI will automatically return an error response.
{
    "name": "Smartwatch",
    "price": 199.9
}

    # @app.post("/items/"):
        # Specifies that this route accepts POST requests at the /items/ endpoint.
        # Used to create or submit new data.
    # Function:
        # The create_item function takes an argument item of type Item (the Pydantic model).
        # FastAPI automatically validates and parses the incoming JSON payload into an Item object.
    # Return Statement:
        # Returns a JSON response containing:
            # A success message with the name of the created item.
            # The item data itself.
@app.post("/items/")
def create_item(item: Item):
    print(Item)
    return {"message": f"Item '{item.name}' has been created!", "data": item}

