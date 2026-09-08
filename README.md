Voter Eligibility Checker

A simple terminal-based Voter Eligibility Checker built with Python. The program allows users to check voter eligibility based on age, register eligible voters by collecting their full name, age, and CNIC, and view basic voting requirements.

This project is designed as a Python practice project for learning functions, user input, conditional statements, loops, input validation, and integer conversion.

Features
Register to vote
Ask for the user's full name
Ask for the user's age
Check voter eligibility
Require voters to be 18 or older
Collect CNIC information from eligible voters
Display registration details
Check voter eligibility separately
Display voting requirements
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


The user is asked to select an option from 1 to 6:

Please select an option (1-6):


If the user enters an invalid choice, the program continues asking until a valid option is entered.

Register to Vote

Select 1 to register to vote.

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


The registration functionality is handled using the function:

def register_voter():


The function collects the user's name and age. If the user is 18 or older, they are asked to enter their CNIC and their registration details are displayed.

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

Check Voter Eligibility

Select 2 to independently check whether a person is eligible to vote.

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

View Voter Details

Option 3 is included in the menu:

3. View voter details


However, the current version of the program does not yet contain functionality for this option.

No elif choice == '3': condition has currently been implemented.

View All Registered Voters

Option 4 is included for viewing all registered voters:

4. View all registered voters


Currently, the program only displays a message:

You have selected to view all registered voters.


The program does not yet store registered voters in a list or other data structure, so multiple voter records cannot currently be displayed.

Voting Requirements

Select 5 to view the basic voting requirements.

The program displays:

You have selected to view voting requirements.
To be eligible to vote, you must:
- Be a citizen of the country
- Be at least 18 years old
- Register to vote before the election


This option is currently implemented directly in the main program.

Exit

Select 6 to exit the program.

The program displays:

Exiting the program. Thank you for using the Voter Eligibility Checker!


The exit option is handled using:

elif choice == '6':
    print("Exiting the program. Thank you for using the Voter Eligibility Checker!")

Menu Validation

The program only accepts menu choices from 1 to 6.

Validation is performed using a while loop:

while choice not in ['1', '2', '3', '4', '5', '6']:
    print("Invalid choice. Please select a valid option (1-6).")
    choice = input("Please select an option (1-6): ")


For example:

Please select an option (1-6): 9
Invalid choice. Please select a valid option (1-6).
Please select an option (1-6): 1


This prevents the program from continuing until the user enters a valid menu choice.

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

After a valid choice is entered, conditional statements determine which operation should be performed:

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

The project is still a beginner-level practice project. The following features are currently planned but not fully implemented:

Option 3 does not display voter details.
Option 4 does not store or display multiple registered voters.
Registered voter information is not saved after the registration function finishes.
There is no database or file storage.
Age input is not yet protected against non-numeric input.
CNIC format validation has not yet been implemented.
The menu currently runs once rather than returning to the menu after completing an operation.
Future Improvements

Possible improvements include:

Store voters in a list or dictionary.
Implement View voter details.
Implement View all registered voters.
Add proper CNIC validation.
Add error handling for invalid age input.
Create a continuous menu loop.
Allow users to register multiple voters.
Save voter information to a file.
Add search functionality for registered voters.
Improve the user interface.
Project Purpose

This project is primarily intended for Python practice and learning. It demonstrates how basic Python concepts can be combined to create a simple interactive terminal application.

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