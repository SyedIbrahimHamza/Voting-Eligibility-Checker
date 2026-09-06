Voter Eligibility Checker

A simple terminal-based Voter Eligibility Checker built with Python. The program allows users to check voter eligibility based on age and register eligible voters by collecting their full name, age, and CNIC.

The project is designed as a Python practice project for learning functions, user input, conditional statements, loops, and input validation.

Features
Register to vote
Ask for the user's full name
Ask for the user's age
Check voter eligibility
Require voters to be 18 or older
Collect CNIC information from eligible voters
Display registration details
Validate menu choices
Display invalid choice messages
Provide options for viewing voter information
Display voting requirements option
Exit option
Menu

The program displays the following menu:

Welcome to Voter Eligibility Checker!
1. Register to vote
2. Check voter eligibility
3. View voter details
4. View all registered voters
5. Voting Requirements
6. Exit


The user is asked to select an option from 1 to 6.

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


The registration function is handled using:

def register_voter():


The function collects the user's information and checks their age before continuing with registration.

Age Eligibility

The program checks whether the user is at least 18 years old.

The condition is:

if age >= 18:


If the age is 18 or older, the user is considered eligible:

You are eligible to register.


The program then asks for the user's CNIC and displays the registration information.

If the user is under 18:

Sorry, you are not eligible to register.
You must be 18 or older.

Voter Details

Option 3 is intended for viewing voter details.

The menu provides:

3. View voter details


The current version of the program does not yet contain the functionality for this option.

View All Registered Voters

Select 4 to view all registered voters.

The current program displays:

You have selected to view all registered voters.


The functionality for storing and displaying multiple registered voters has not yet been implemented.

Voting Requirements

Option 5 is provided for voting requirements:

5. Voting Requirements


The current version displays the option in the menu, but the functionality for showing voting requirements has not yet been implemented.

Exit

Option 6 is provided to exit the program.

6. Exit


The exit functionality is included in the menu, but the current version does not yet contain an elif condition to handle option 6.

Menu Validation

The program only accepts menu choices from 1 to 6.

The validation is performed using:

while choice not in ['1', '2', '3', '4', '5', '6']:
    print("Invalid choice. Please select a valid option (1-6).")
    choice = input("Please select an option (1-6): ")


For example:

Please select an option (1-6): 9
Invalid choice. Please select a valid option (1-6).
Please select an option (1-6): 1


This prevents the program from continuing until the user enters a valid menu option.

Program Logic

The program first displays the welcome message and menu:

print("Welcome to Voter Eligibility Checker!")


It then asks the user to select an option:

choice = input("Please select an option (1-6): ")


The program validates the choice using a while loop.

After a valid choice is entered, conditional statements determine which operation should be performed:

if choice == '1':
    register_voter()
elif choice == '2':
    print("You have selected to check voter eligibility.")
elif choice == '4':
    print("You have selected to view all registered voters.")

Python Concepts Used

This project practices several Python fundamentals:

Functions
Function calls
if, elif, and else
while loops
while with membership checking
User input with input()
Integer conversion with int()
String comparison
Lists
Conditional operators