from entity.Expense import Expense
from database import connect

db_connection = connect.connect()

def get_all_expenses():
    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM expenses ORDER BY date desc, exp_id")
        row = cursor.fetchone()
        arr = []
        while row is not None:
            arr.append(row)
            row = cursor.fetchone()
        return arr
    except Exception as error:
        print("APP ERROR:", error)
        return error

def add_expense(expense: Expense):
    try:
        cursor = db_connection.cursor()
        cursor.execute("insert into expenses (title, amount, date, involved_people, split_style, category, create_nm)  "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (expense.title, expense.amount, expense.date, expense.involved_people, expense.split_style, expense.category, expense.create_nm))
        db_connection.commit()
        return True
    except Exception as error:
        print("APP ERROR:", error)
        return error


def delete_expense(exp_id: int):
    try:
        cursor = db_connection.cursor()
        cursor.execute("delete from expenses where exp_id = %s", [exp_id])
        db_connection.commit()
        return cursor.rowcount
    except Exception as error:
        print("APP ERROR:", error)
        return error

def update_expense(expense: Expense):
    try:
        cursor = db_connection.cursor()
        # update row
        cursor.execute("update expenses set title = %s, amount = %s, date = %s, involved_people = %s, split_style = %s, category = %s, create_nm = %s "
                       "where exp_id = %s",
                       (expense.title, expense.amount, expense.date, expense.involved_people, expense.split_style, expense.category, expense.create_nm, expense.exp_id))
        db_connection.commit()

        #get newly updated row
        cursor.execute("SELECT * FROM expenses where exp_id = %s", [expense.exp_id])
        return cursor.fetchone()
    except Exception as error:
        print("APP ERROR:", error)
        return error


