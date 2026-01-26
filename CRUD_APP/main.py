from fastapi import FastAPI,HTTPException
from models import Employee
from typing import List

employees_db:list[Employee]=[]

app=FastAPI()

# Read Employee data
@app.get('/employees',response_model=List[Employee])
def get_employees():
    return employees_db

@app.get('/employees/{id}',response_model=Employee)
def get_employee(id:int):
    for employee in employees_db:
        if employee.id==id:
            return employee
    raise HTTPException(status_code=404,detail='Employee Not found')

# Create Employee data

@app.post('/add_employee',response_model=Employee)
def add_employee(new_employee:Employee):
    for employee in employees_db:
        if employee.id==new_employee.id:
            raise HTTPException(status_code=400,detail='Employee already exists')

    employees_db.append(new_employee)
    return new_employee

# Update Employee data

@app.put('/update_employee/{id}',response_model=Employee)
def update_employee(id:int,updated_employee:Employee):
    for index,employee in enumerate(employees_db):
        if employee.id==id:
            employees_db[index]=updated_employee
            return updated_employee
    raise HTTPException(status_code=404,detail='Employee Not Found')

# Delete an Employee
@app.delete('/delete_employee/{emp_id}')
def delete_employee(id:int):
    for index,employee in enumerate(employees_db):
        if employee.id==id:
            del employees_db[index]
            return {'message':f"Employee with id: {id} is deleted"}
    raise HTTPException(status_code=404,detail='Employee Not Found')