from flask import Flask, request
from flask_smorest import Api
import json
from user.admin_page import Admin

app = Flask(__name__)

admin = Admin("tbhowmick")

@app.get("/employee")
def get_all_employee_details():
    employees = admin.display_all_emp_details()
    return {"employees": employees}

@app.post("/employee")
def add_new_employee():
    request_data = request.get_json()
    new_employee = {
        "emp_name": request_data["emp_name"],
        "username": request_data["username"],
        "emp_id": request_data["emp_id"],
        "age": request_data["age"],
        "role": request_data["role"],
        "dept": request_data["dept"],
        "salary": request_data["salary"]
    }
    admin.add_employee(new_employee)
    return new_employee, 201

@app.delete("/employee/<string:username>")
def delete_employee(username):
    return admin.remove_employee(username), 201