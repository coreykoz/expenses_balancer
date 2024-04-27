from fastapi import FastAPI, HTTPException
from service import ExpenseService
from entity.Expense import Expense
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/expense/getall")
def get_all_expenses():
    return {'data': ExpenseService.get_all_expenses()}

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
