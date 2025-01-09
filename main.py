# Importing Required Modules:
from fastapi import FastAPI # FastAPI: Used to build the API framework.
from pydantic import BaseModel # Pydantic.BaseModel: Provides data validation and parsing. Used to define the structure of the Course model.
from typing import Optional # Optional: Allows fields to be optional (i.e., can be None).

# Initializing the FastAPI App:
app = FastAPI() # The FastAPI() instance app serves as the entry point for defining and managing API routes.

# Fake Database:
fakedb = [] # This is a simple list acting as an in-memory database for storing course information. It stores courses as dictionaries.

# Pydantic Model for Course:
class Course(BaseModel): # Course defines the structure and validation rules for incoming course data.
    id: int
    name: str
    price: float
    is_early_bird: Optional[bool] = None

# API Routes:
    # Root Endpoint
        # GET /: Root endpoint that returns a greeting message.
@app.get("/")
def read_root():
    return {"greetings": "Welcome to LearnCodeOnline.in"}

        # GET /courses:
            # Returns all courses in the fakedb list.
            # Initially, fakedb is empty, so this will return an empty list.
@app.get("/courses")
def get_courses():
    return fakedb

        # GET /courses/{course_id}:
            # Fetches a single course by its ID.
            # The course_id is used as an index after subtracting 1 (since list indices start at 0).
            # If the course doesn't exist, this will raise an index out of range error.
@app.get("/courses/{course_id}")
def get_a_course(course_id: int):
    course = course_id - 1
    return fakedb[course]

        # POST /courses:
            # Adds a new course to the fakedb list.
            # Converts the Course object into a dictionary using .dict() before appending.
            # Returns the newly added course.
@app.post("/courses")
def add_course(course: Course):
    fakedb.append(course.dict())
    return fakedb[-1]

        # DELETE /courses/{course_id}:
            # Removes a course from fakedb using its index (course_id - 1).
            # Returns a success message after deletion. 
@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    fakedb.pop(course_id - 1)
    return {"task": "deletion successful"}

# "greetings": A static message for the root endpoint.
# "data": An example payload of a course.
{
    "greetings": "Welcome to LearnCodeOnline.in",         
    "data":{                                               
        "id": 1,
        "name" : "Python Basics",
        "price" : 199.99,
        "is_early_bird" : True
    }
}

{
    "greetings": "Welcome to LearnCodeOnline.in",

    "data":{
        "id": 2,
        "name": "JavaScript Advanced",
        "price": 299.99,
        "is_early_bird": False

    }
}

# Key Notes:
    # Dynamic Path Parameters:
        # {course_id} is dynamically extracted from the URL.
    # Validation:
        # FastAPI automatically validates incoming requests using the Course Pydantic model.
    # Optional Fields:
        # is_early_bird is optional, meaning it can be omitted in requests.
    # Database Simulation:
        # fakedb simulates a database. It stores all data in-memory and is not persistent.
    # Indexing Issue:
        # Subtracting 1 from course_id assumes that IDs start at 1, which may lead to errors if the course ID is invalid or doesn't exist.
