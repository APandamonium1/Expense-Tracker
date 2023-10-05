import math
import csv
from datetime import date

column_headings = ['No.', 'Date', 'Amount ($)', 'Description', 'Category']
categories = {'Food': 0,
              'Transportation': 0,
              'Shopping': 0,
              'Others': 0}
expenses_list = []  # all the expenses joined into a single list


# --------------------------
#    Displays the main menu
# --------------------------
def menu():
    menu_printList = input("""What would you like to do?
        1] View all expenses
        2] Add an expense
        3] Delete an expense
        4] Edit an expense
        5] Analyse expenses
        6] Search expenses
        Choice: 
        """)

    choice_list = {
        "1": "View expenses",
        "2": "Add an expense",
        "3": "Delete an expense",
        "4": "Edit and expense",
        "5": "Analyse expenses",
        "6": "Search expenses"
    }

    choice = choice_list.get(menu_printList, "Please input correct choice.")

    # print("1. View expenses")
    # print("2. Add expense")
    # print("3. Delete expense")
    # print("4. Edit expense")
    # print("5. Analyse expenses")
    # print("6. Search expenses")
    # choice = int(input('Your choice? '))
    return choice


# --------------------------------------
# display all records in tabular format
# or choose to view only one
# if no expenses, say so
# --------------------------------------
def viewExpense():
    view_choice = int(input("Which expense would you like to view? "))
    if view_choice <= len(expenses_list):
        print(expenses_list[view_choice - 1])
    elif view_choice == 0:
        for i in expenses_list:
            print(i)


# -------------------------------------------------------------------------
# user input for date
# user input for description of expense
# user input for amount as float
# additional: load a standard set of descriptions (.txt) for ease of input
# -------------------------------------------------------------------------
def addExpense():
    # adding in details for new expense
    date_detail = input('Date of expense (dd/mm/yyyy): ')
    date_split = date_detail.split('/')
    date_object = date(int(date_split[2]), int(date_split[1]), int(date_split[0]))

    amount = float(input('Expense amount ($): '))

    description_detail = input("Description of  expenses: ")

    # category choices
    print(" ------------")
    print("| Categories |")
    print(" ------------")

    # add new expense to expenses_list
    return date_object, amount, description_detail, expenses_list


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
print(" EXPENSES TRACKER")
print("------------------")
print()
while True:
    new_old_choice = input("New set of expenses or open currently stored? (New/Current): ")
    if new_old_choice == 'Current':
        loadExpense()
    elif new_old_choice == 'New':
        initialiseExpense()

    # displays main menu & prompt for user's choice
    main_choice = menu()
    if main_choice == 1:
        viewExpense()
    elif main_choice == 2:
        addExpense()
    elif main_choice == 3:
        deleteExpense()
    elif main_choice == 4:
        editExpense()
    elif main_choice == 5:
        analyseExpense()
    elif main_choice == 6:
        searchExpense()

    break

