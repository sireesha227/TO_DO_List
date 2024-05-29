# TO-DO LIST
#### Video Demo:  <https://youtu.be/Tse4H3Dcd1M>
#### Description:
This project focus on developing a simple text based to-do list manager that allows the users to interact with there tasks through a command line interface. This application is designed to be lightweight, easy to use and accessible from the terminal.It enables the users to add,delete,update or view to-do tasks.

I used sqlite3 for the database, created tasks.db as the database and TASKS table for storing the tasks.

Tabulate library for creating formatted tables from Tasks database. It helps in visually presenting tabular data in a structured and readable format.

pyfiglet library is a Python wrapper for the FIGlet, a program that generates text banners in various typefaces composed of letters made up of conglomerations of smaller ASCII characters. FIGlet is commonly used for creating stylized text, such as ASCII art, banners, and decorative text, especially in the context of command-line interfaces.

We used figlet to show "Welcome" text for the application.Here we used "big" font for welcome.

The user should select a number between 1 to 5 to perform any task like creating a task, deleting a task updating a task, show all task or exit respectively.

The task_description can't be null for updating or inserting the tasks.To update or delete a task, please enter the task_id those are present in the database only.

Assumptions:

1) Task_descripition can't be null, if it null then it will not insert or update the tasks
2) User should only enter the task_id that are present in the table for delete or update the tasks.
3) The user must give the inputs as per the app requirements only.


