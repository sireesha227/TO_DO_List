import time
import sys
import sqlite3
from tabulate import tabulate
from pyfiglet import Figlet

# Main function
def main():
    #It will connect to the data base and create a table called TASKS
    database = connect_database()
    query_stat = create_table(database)

    # Takes input from the user until he chooses to exit
    while True:
        task = get_user_input()

        if not validate_task(task):
            print("\nPlease select appropriate options.")
        else:
            perform_task(task,database)


# It will take an input from the user and returns the input
def get_user_input():
    print("\n1. Create a Task\n2. Delete a Task\n3. Update a Task\n4. Show all Tasks\n5. Exit\n")
    operation = int(input("What you want to do? Select an option from above: "))
    print()
    return operation

# It will validate the input entered by the user and returns True or False
def validate_task(task):
    if 0 < task < 6:
        return True
    return False

# Based on the user input it will performs a specific task
def perform_task(task,db):
    if task == 1:
        create_task(db)
        proceed_or_not()

    elif task == 2:
        delete_task(db)
        proceed_or_not()

    elif task == 3:
        update_task(db)
        proceed_or_not()

    elif task == 4:
        show_tasks(db)
        proceed_or_not()

    elif task == 5:
        close_connection(db)
        sys.exit("Thankyou!!!\n")

# It will check do we need to proceed further or not
def proceed_or_not():
    proceed = input("\nDo you want to proceed further (Y/N)? ")
    if proceed.lower() not in ['y','yes']:
        sys.exit("\nThankyou!!!\n")

# It will create a task
def create_task(db):
    task_description = input("Task_Description: ")
    entry_time = get_current_time()

    # Insert a task into the table for task creation
    if len(task_description) > 0:
        query_task =insert_into_table(db,task_description,entry_time)
        print(query_task)
    else:
        print("\nPlease add description of the task")

# It returns the current time in DD/MM/YY HH:MM:SS format
def get_current_time():
    # current time
    local_time = time.localtime()
    current_time = time.strftime("%m/%d/%Y %H:%M:%S", local_time)
    return current_time

# It will delete the task from the table
def delete_task(db):
    # Show all the tasks in the table using cursor
    show_tasks(db)

    #Take the task_id from the user that needs to be deleted
    task_id = int(input("\nEnter Task_Id you want to delete from above table: "))

    # Delete the row based on the given task_id
    query_status = delete_task_db(db,task_id)
    print(query_status)

# It will update the task
def update_task(db):
    # Show all the tasks in the table using cursor
    show_tasks(db)

    task_id = int(input("\nEnter Task_Id you want to update from above table: "))
    update_task_desc = input("\nTask Description: ")

    # update the row based on the task ID and given new Task
    if len(update_task_desc) > 0:
        query_status = update_table(db,task_id,update_task_desc,get_current_time())
        print(query_status)
    else:
        print("\nPlease add description of the task")

# It will show all the tasks in the database
def show_tasks(db):
    cursor = read_table(db)
    cursor_list = []
    headers = ["SNO","Task_ID","Task_Description","Created_Date"]
    maxcol_len = [None,None,50,None]
    for row in cursor:
        row_list = list(row)
        cursor_list.append(row_list)
    if len(cursor_list) > 0:
        print(tabulate(cursor_list,headers,tablefmt="grid",showindex="always",maxcolwidths=maxcol_len))
    else:
        print("You Dont have any tasks. Feel free to add one!!😊")


## Queries for Database
# It will connect to the database tasks.db
def connect_database():
    db = sqlite3.connect("tasks.db")
    return db

# Query for creating table
def create_table(db):
    try:
        db.execute('''CREATE TABLE IF NOT EXISTS TASKS
               (TASKID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               TASK TEXT NOT NULL,
               ENTRYDATE TIMESTAMP NOT NULL);''')
        db.commit()
        return "\nTable created successfully!!!"
    except sqlite3.Error:
        return "\nError, table not created"

# Query for deleting table
def delete_table(db):
    try:
        db.execute("DROP TABLE TASKS;")
        db.commit()
        return "\nTable Deleted Successfully!!!"
    except sqlite3.Error:
        return "\nError, while deleting the table"

# Query for deleting task
def delete_task_db(db,task_id):
    try:
        db.execute("DELETE FROM TASKS WHERE TASKID = ?",(task_id,))
        db.commit()
        return "\nSuccessfully deleted the task!!!"
    except sqlite3.Error:
        return "\nError, while deleting the task!!!"

# Query for select data from table
def read_table(db):
    cursor = db.execute("SELECT * FROM TASKS;")
    return cursor

# Query for inserting data into table
def insert_into_table(db,task,entrydate):
    try:
        db.execute("""INSERT INTO TASKS(TASK,ENTRYDATE)
               VALUES (?,?);""",(task,entrydate))
        db.commit()
        return "\nTask added successfully!!!"
    except sqlite3.Error as e:
        print(e.sqlite_errorname)
        return "\nError while adding the task!!!"


# Query for updating the table
def update_table(db,task_id,task,entrydate):
    try:
        db.execute("""UPDATE TASKS set TASK = ?,ENTRYDATE = ? WHERE TASKID = ?;""", (task,entrydate,task_id))
        db.commit()
        return "\nTask updated successfully"
    except sqlite3.Error:
        return "\nError while updating the task!!!"

# Closes the database connection
def close_connection(db):
    db.close()

if __name__ == "__main__":
    print()
    #figlet is used to format the text
    figlet = Figlet()
    figlet.setFont(font='big')
    print(figlet.renderText("WELCOME"))
    main()
