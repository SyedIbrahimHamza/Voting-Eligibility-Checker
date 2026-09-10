Voter Eligibility Checker

A simple terminal-based Voter Eligibility Checker built with Python. The program allows users to check voter eligibility based on age, register eligible voters by collecting their full name, age, and CNIC, and view basic voting requirements.

This project is designed as a beginner-level Python practice project for learning:

Functions
User input
Conditional statements
if, elif, and else
while loops
Input validation
Integer conversion
String comparison
Basic program flow
Features

The current version of the program includes:

Register to vote
Ask for the user's full name
Ask for the user's age
Check voter eligibility
Require voters to be 18 or older
Collect CNIC information from eligible voters
Display registration details
Check voter eligibility separately
Display basic voting requirements
Validate menu choices
Display invalid choice messages
Exit the program
Menu

When the program starts, it displays the following menu:

Welcome to Voter Eligibility Checker!
1. Register to vote
2. Check voter eligibility
3. View voter details
4. View all registered voters
5. Voting Requirements
6. Exit


The user is asked to select an option:

Please select an option (1-6):


The program validates the menu choice and only accepts options from 1 to 6.

If an invalid choice is entered, the program continues asking until a valid option is entered.

Example:

Please select an option (1-6): 9
Invalid choice. Please select a valid option (1-6).
Please select an option (1-6): 1

Register to Vote

Select option 1 to register to vote.

The program asks for:

Full name
Age
CNIC

Example:

Please select an option (1-6): 1
You have selected to register to vote.
Please enter your full name: Ali Ahmed
Please enter your age: 25
You are eligible to register.
Please enter your CNIC: 42101-1234567-1

Registration Successful!
Name: Ali Ahmed
Age: 25
CNIC: 42101-1234567-1


The registration functionality is handled using the register_voter() function:

def register_voter():


The function collects the user's name and age.

If the user is 18 or older, they are considered eligible to register and are asked to provide their CNIC.

The registration details are then displayed.

Age Eligibility

The program considers a person eligible if they are 18 years old or older.

The condition used is:

if age >= 18:


If the age is 18 or older:

You are eligible to register.


The program then asks for the user's CNIC.

If the user is under 18:

Sorry, you are not eligible to register.
You must be 18 or older.


The same age requirement is used when independently checking voter eligibility.

Check Voter Eligibility

Select option 2 to independently check whether a person is eligible to vote.

The program asks the user to enter their age.

Example:

Please select an option (1-6): 2
You have selected to check voter eligibility.
Please enter your age: 20
You are eligible to vote.


For someone under 18:

Please enter your age: 16
Sorry, you are not eligible to vote.
You must be 18 or older.


The eligibility check uses:

if age >= 18:
    print("You are eligible to vote.")
else:
    print("Sorry, you are not eligible to vote.")
    print("You must be 18 or older.")

View Voter Details

Option 3 is included in the menu:

3. View voter details


However, the current version of the program does not implement this option.

There is currently no:

elif choice == '3':


condition in the program.

Therefore, selecting option 3 does not display voter details or produce any additional output.

View All Registered Voters

Option 4 is included in the menu:

4. View all registered voters


The current program only displays:

You have selected to view all registered voters.


The program does not currently store registered voters in a list, dictionary, or other data structure.

As a result, multiple voter records cannot currently be viewed.

Voting Requirements

Select option 5 to view the basic voting requirements.

The program displays:

You have selected to view voting requirements.
To be eligible to vote, you must:
- Be a citizen of the country
- Be at least 18 years old
- Register to vote before the election


This functionality is currently implemented directly in the main program.

Exit

Select option 6 to exit the program.

The program displays:

Exiting the program. Thank you for using the Voter Eligibility Checker!


The exit option is handled using:

elif choice == '6':
    print("Exiting the program. Thank you for using the Voter Eligibility Checker!")

Menu Validation

The program validates the user's menu selection using a while loop:

while choice not in ['1', '2', '3', '4', '5', '6']:
    print("Invalid choice. Please select a valid option (1-6).")
    choice = input("Please select an option (1-6): ")


This ensures that the program does not continue until the user enters one of the valid menu choices.

Program Logic

The program first displays the welcome message and menu:

print("Welcome to Voter Eligibility Checker!")
print("1. Register to vote")
print("2. Check voter eligibility")
print("3. View voter details")
print("4. View all registered voters")
print("5. Voting Requirements")
print("6. Exit")


It then asks the user to select an option:

choice = input("Please select an option (1-6): ")


The choice is validated using a while loop.

After a valid choice is entered, if and elif statements determine which operation should be performed:

if choice == '1':
    register_voter()

elif choice == '2':
    # Check voter eligibility

elif choice == '4':
    # View all registered voters

elif choice == '5':
    # Display voting requirements

elif choice == '6':
    # Exit program


There is currently no implementation for option 3.

Python Concepts Used

This project practices several Python fundamentals:

Functions
Function calls
if, elif, and else statements
while loops
Membership checking with in
User input with input()
Integer conversion with int()
String comparison
Lists
Conditional operators
Basic program flow
Current Limitations

The project is still a beginner-level practice project. The current limitations are:

Option 3 does not display voter details.
Option 4 does not store or display registered voters.
Registered voter information is only displayed during registration and is not stored.
There is no database or file storage.
Age input is not protected against non-numeric input.
Invalid age input will cause the program to terminate because int() is used without exception handling.
CNIC format validation has not been implemented.
The menu runs only once.
Users cannot register multiple voters in a single program run.
There is no search functionality for registered voters.
Future Improvements

Possible improvements include:

Store voters in a list or dictionary.
Implement the View voter details option.
Implement View all registered voters.
Add CNIC format validation.
Add error handling for invalid age input.
Create a continuous menu loop.
Allow users to register multiple voters.
Save voter information to a file.
Add search functionality for registered voters.
Improve the terminal user interface.
Organize the program into separate functions for each menu option.
Project Purpose

This project is primarily intended for Python practice and learning.

It demonstrates how basic Python concepts can be combined to create a simple interactive terminal application.

The project is useful for practicing user input, functions, conditional logic, loops, validation, and basic program structure.

Example

A typical registration process looks like:

Welcome to Voter Eligibility Checker!
1. Register to vote
2. Check voter eligibility
3. View voter details
4. View all registered voters
5. Voting Requirements
6. Exit

Please select an option (1-6): 1
You have selected to register to vote.
Please enter your full name: Ali Ahmed
Please enter your age: 25
You are eligible to register.
Please enter your CNIC: 42101-1234567-1

Registration Successful!
Name: Ali Ahmed
Age: 25
CNIC: 42101-1234567-1

License

This project is intended for educational and practice purposes.