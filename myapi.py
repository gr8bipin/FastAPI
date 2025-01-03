from fastapi import FastAPI

app = FastAPI()

# amazon.com/create-user

# GET - GET AN INFORMATION
# POST - CREATE SOMETHING NEW
# PUT - UPDATE
# DELETE - DELETE SOMETHING


students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}

@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]
    
# google.com/get-student/1