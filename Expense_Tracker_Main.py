import math
import csv
from datetime import date

column_headings = ['No.', 'Date', 'Amount ($)', 'Description', 'Category']
categories = {'Food': 0,
              'Transportation': 0,
              'Shopping': 0,
              'Others': 0}


# --------------------------
#    Displays the main menu
# --------------------------
def menu():
    pass


# --------------------------------------
# display all records in tabular format
# if no expenses, say so
# --------------------------------------
def viewExpense():
    pass


# -------------------------------------------------------------------------
# user input for date
# user input for description of expense
# user input for amount as float
# additional: load a standard set of descriptions (.txt) for ease of input
# -------------------------------------------------------------------------
def addExpense():
    date_detail = input('Date of expense (dd/mm/yyyy): ')
    date_split = date_detail.split('/')
    date_object = date(int(date_split[2]), int(date_split[1]), int(date_split[0]))

    amount = float(input('Expense amount ($): '))

    description_detail = input("Description of expenses: ")
    return date_object, amount, description_detail


def deleteExpense():
    delete_choice = int(input('Expenses no. to be deleted: '))
    pass


def editExpense():
    edit_choice = int(input('Please select the expense to be edited: '))
    pass


# ------------------------------------------------------------------------------------------------------
# total expenses: sum up all expenses and display
# average daily expenses: calculate and display average daily expenses
# expenses for data range: allow the user to input a date range and display expenses within that range
# ------------------------------------------------------------------------------------------------------
def analyseExpense():
    pass




def searchExpense():
    pass


# -------------------------------------------------
#    Saves the expenses in the file 'expenses.txt'
# -------------------------------------------------
def saveExpense():
    pass


# ------------------------------------------
#    Loads the expenses from 'expenses.txt'
# ------------------------------------------
def loadExpense():
    pass


# ------------------------------------------------
#    Initializes all the variables for a new set
# ------------------------------------------------
def initialiseExpense():
    pass


'''
Optional Enhancements:

- For categorizing expenses, you can create a dictionary where categories are keys,
and the values are lists of expenses associated with those categories.
- For the search feature, implement a function that allows the user to search for
expenses by date or description. Display the results in a list.
- To create charts or graphs for visualizing expense trends, consider using Python
libraries like Matplotlib or Plotly. You'll need to collect and process the data accordingly.
'''

# -----------------------------------------
#               MAIN APP
# -----------------------------------------
print("Expenses Tracker")
print("----------------")
print()
while True:
    # displays main menu & prompt for user's choice
    main_choice = menu()