
# Importing FastAPI:
    # FastAPI is a framework for building APIs quickly and efficiently.
    # FastAPI is imported to create the application and define routes.
from fastapi import FastAPI

# Initializing the App:
    # FastAPI() initializes the application instance named app, which acts as the entry point for the API.
    # This app serves as the central point to define and manage all API routes and settings.
    # When you run the application, this instance will handle incoming HTTP requests and route them to the appropriate functions.
app = FastAPI()

# Data Storage (Students Dictionary):
    # This is a simple dictionary named students, which serves as in-memory data storage for the API.
    # Each key (e.g., 1) represents a unique student ID, and the value is another dictionary containing student details like name, age, and class.
students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}

# Routing:
    # The root endpoint (/) and the /get-student/{student_id} endpoint showcase how FastAPI handles different URL routes.

# Path Parameters:
    # {student_id} is an example of a path parameter used to dynamically retrieve specific data.

# Returning JSON:
    # FastAPI automatically converts Python dictionaries (e.g., {"name": "First Data"}) to JSON format in HTTP responses.

# Type Validation:
    # student_id: int ensures that the input provided for student_id is an integer. If a non-integer is provided, FastAPI will return an automatic validation error.

# Defining the Root Endpoint
    # @app.get("/") defines an HTTP GET endpoint at the root URL (/).
    # When a user visits the root URL of the API, the index function is executed, returning the JSON response {"name": "First Data"}.
        # How it works:
            # @app.get("/"): Decorator that specifies the route (/) and HTTP method (GET).
                # def index(): Function executed when the root endpoint is accessed.
                # return {"name": "First Data"}: Returns a JSON object to the client.

                # Example Response:
                    # (json)
                    # {
                    #   "name": "First Data"
                    # }
@app.get("/")
def index():
    return {"name": "First Data"}

# Fetching a Specific Student's Data:
    # This defines another HTTP GET endpoint that allows users to retrieve student data by their student_id.
    # How it works:
        # @app.get("/get-student/{student_id}"):
            # Specifies the route /get-student/{student_id}.
            # {student_id} is a path parameter, meaning it changes dynamically based on the user’s request.
        # def get_student(student_id: int)::
            # The function accepts student_id as an integer parameter.
            # The student_id provided in the URL is automatically passed to this function.
        # return students[student_id]:
            # The function looks up the student_id in the students dictionary and returns the corresponding data.
@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]
    
# Example Request:
    # (sql)
        # GET /get-student/1

# Example Response:
    # (json)
        # {
        #   "name": "john",
        #    "age": 17,
        #    "class": "year 12"
        # }
