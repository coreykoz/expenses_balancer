from entity.Expense import Expense
from database import connect
import constants

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

def get_all_unpaid_expenses():
    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM expenses ex WHERE ex.paid = false ORDER BY date desc, exp_id")
        row = cursor.fetchone()
        arr = []
        while row is not None:
            arr.append(row)
            row = cursor.fetchone()
        return arr
    except Exception as error:
        print("APP ERROR:", error)
        return error

def validate_added_expense(expense: Expense):
    corey_involved = constants.corey in expense.involved_people
    anna_involved = constants.anna in expense.involved_people

    if constants.split_style_map[expense.split_style] == constants.split_style_1_text or constants.split_style_map[expense.split_style] == constants.split_style_3_text:
        return corey_involved and anna_involved
    return (corey_involved and not anna_involved) or (anna_involved and not corey_involved)


def add_expense(expense: Expense):
    if not validate_added_expense(expense):
        print("Validation ERROR: Expense does not have proper parties involved for split style")
        return False
    try:
        cursor = db_connection.cursor()
        cursor.execute("insert into expenses (title, amount, date, involved_people, split_style, category, create_nm, paid)  "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, false)",
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
        cursor.execute("update expenses set title = %s, amount = %s, date = %s, involved_people = %s, split_style = %s, category = %s, create_nm = %s, paid = %s "
                       "where exp_id = %s",
                       (expense.title, expense.amount, expense.date, expense.involved_people, expense.split_style, expense.category, expense.create_nm, expense.paid, expense.exp_id))
        db_connection.commit()

        #get newly updated row
        cursor.execute("SELECT * FROM expenses where exp_id = %s", [expense.exp_id])
        return cursor.fetchone()
    except Exception as error:
        print("APP ERROR:", error)
        return error

def get_summary(self):
    unpaid_expenses = self.get_all_unpaid_expenses()
    running_total = 0
    if unpaid_expenses != null:
        for expense in unpaid_expenses:
            value_to_modify = 1

            # corey is postive numbers, anna is negative numbers
            # figure out who made expense
            running_total += value_to_modify

