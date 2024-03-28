from fastapi import FastAPI, HTTPException
from service import ExpenseService
from entity.Expense import Expense

app = FastAPI()

@app.get("/expense/getall")
def get_all_expenses():
    return {'response': ExpenseService.get_all_expenses()}

@app.get("/expense/getallUnpaid")
def get_all_expenses():
    return {'response': ExpenseService.get_all_unpaid_expenses()}

@app.post("/expense/add")
async def add_expense(exp: Expense):
    return {'response': ExpenseService.add_expense(exp)}

@app.delete("/expense/delete")
def delete_expense(exp_id: int):
    return {'response': ExpenseService.delete_expense(exp_id)}

@app.put("/expense/update")
def update_expense(exp: Expense):
    return {'response': ExpenseService.update_expense(exp)}

@app.get("/expense/getSummary")
def get_all_expenses():
    return {'response': ExpenseService.get_summary()}
