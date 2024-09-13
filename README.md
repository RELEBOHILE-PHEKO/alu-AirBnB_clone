# AirBnB Clone - Command Interpreter

## Description
This project is the first step toward building a full web application similar to the AirBnB platform. The command interpreter is a basic console that manages AirBnB objects such as `User`, `Place`, `City`, and more. It allows you to create, update, and manage these objects, with functionalities such as saving them to a JSON file and loading them back.

## Command Interpreter
The command interpreter is a command-line interface (CLI) application built using Python's `cmd` module. It allows you to manage different types of AirBnB objects.

    ## Start the command interpreter
 ./console.py

     How to Use It
Once the interpreter is running, you can use the following commands:

create <class>: Creates a new instance of the specified class and saves it.
show <class> <id>: Displays the given class instance with the specified ID.
destroy <class> <id>: Deletes the class instance with the given ID.
all <class>: Displays all instances of the specified class.
quit: Exits the command interpreter
         Example
Create a new user: create User email="lebo@yahoo.com" password="246@ypd"
Show information about a user: show User 120
Delete a user: destroy User 120
