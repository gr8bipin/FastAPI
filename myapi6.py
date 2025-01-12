# Response Model

# This code defines a FastAPI application where an endpoint is created to receive and return data 
# using Pydantic models for validation. 

from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

# PackageIn and Package are pydantic models

class PackageIn(BaseModel): # PackageIn represents the input model for creating a package.
    secret_id: int # Includes a secret_id field that might be sensitive and not intended for public response.
    name: str # Required string field for the name of the package.
    number: str # Required string field for a unique identifier.
    description: Optional[str] = None # Optional string field for additional details about the package.


# Package represents the output model (the response model).
# Omits secret_id to avoid exposing sensitive information.
# name, number, and description are the same as in PackageIn.
class Package(BaseModel): 
    name: str
    number: str
    description: Optional[str] = None

app = FastAPI()  # Initializes the FastAPI app instance

# Purpose: A simple "hello world" endpoint for testing if the app is working.
@app.get("/") # Route: / (root endpoint). # Method: GET. 
async def hello_world():
    return {'Hello': 'World'} # Returns a JSON response {'Hello': 'World'}.


# @app.post("/package/"):

    # Route: /package/ (endpoint to handle package creation).
    # Method: POST.
    # Request Body:
        # Takes input of type PackageIn (as defined in the function parameter package: Package).
    # Response:
        # Uses response_model=Package to ensure the output is shaped according to the Package model.
        # Since response_model_include is used, the response will only include the description field from the Package model. If description is not provided, the response will be empty ({}).
@app.post("/package/", response_model = Package, response_model_include = {"description"}) # path parameters
async def make_package(package: PackageIn):
    return Package(name=package.name, number=package.number, description=package.description)
