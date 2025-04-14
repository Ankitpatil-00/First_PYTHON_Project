import sqlite3 as sq

conn = sq.connect('Daily_Expenses.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS daily_expense(
          Date TEXT,
          Food REAL,
          Travel REAL,
          Other REAL,
          Total_Expense REAL)""")

conn.commit()
conn.close()

def View_Database():
    conn = sq.connect('Daily_Expenses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM daily_expense")
    data = c.fetchall()
    print("\nDate       | Food  | Travel | Other | Total")
    print("---------------------------------------------")
    for row in data:
        print(f"{row[0]:<11}| {row[1]:<6}| {row[2]:<7}| {row[3]:<6}| {row[4]}")
    conn.close()
    print("\n")

def Update_Database():
    date = input("Enter the date you want to update (YYYY-MM-DD): ")
    amount1 = Food()
    amount2 = Travel()
    amount3 = Other()
    total_amount = amount1 + amount2 + amount3
    Update(date, amount1, amount2, amount3, total_amount)

def Update(date, amount1, amount2, amount3, total_amount):
    conn = sq.connect('Daily_Expenses.db')
    c = conn.cursor()
    c.execute(""" 
              UPDATE daily_expense 
              SET Food = ?, Travel = ?, Other = ?, Total_Expense = ?
              WHERE Date = ?""",
              (date, amount1, amount2, amount3, total_amount))
    conn.commit()
    conn.close()
    print("\nExpense Updated:")
    print(f"Date: {date}")
    print(f"Food: {amount1}")
    print(f"Travel: {amount2}")
    print(f"Other: {amount3}")
    print(f"Total_Expense: {total_amount}")
    print("\n")
    
def Insert(date, amount1, amount2, amount3, total_amount):
    conn = sq.connect('Daily_Expenses.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO daily_expense (Date, Food, Travel, Other, Total_Expense) VALUES (?, ?, ?, ?, ?)",
                  (date, amount1, amount2, amount3, total_amount)
     )
    conn.commit()
    conn.close()
    print("\nExpense Summary:")
    print(f"Date: {date}")
    print(f"Food: {amount1}")
    print(f"Travel: {amount2}")
    print(f"Other: {amount3}")
    print(f"Total_Expense: {total_amount}")

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    amount1 = Food()
    amount2 = Travel()
    amount3 = Other()
    total_amount = amount1 + amount2 + amount3

    Insert(date, amount1, amount2, amount3, total_amount)
    print("\n")

def Food():
    amount1 = int(input("Enter Todays Food Expense: "))
    return amount1
   
def Travel():
    amount2 = int(input("Enter Todays Travel Expense: "))
    return amount2

def Other():
    amount3 = int(input("Enter Todays Other Expense: "))
    return amount3

def Delete():
    conn = sq.connect('Daily_Expenses.db')
    c = conn.cursor()
    c.execute("DELETE FROM daily_expense")
    conn.commit()
    print("Database Delete Successfully")

while True:
    print("Welcome to Expense Management System")
    print("1. Add Expense")
    print("2. Update Expense")
    print("3. View Database")
    print("4. Delete Datbase")
    print("5. Exit")
    choice = input("Enter your choice (1 or 2 or 3 or 4 or 5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        Update_Database()
    elif choice == "3":
        View_Database()
    elif choice == "4":
        Delete()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break    
    else:
        print("Invalid choice!")

