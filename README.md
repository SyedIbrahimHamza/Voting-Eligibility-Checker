Voter Eligibility Checker

A simple terminal-based Voter Eligibility Checker built with Python. The program allows users to register eligible voters, validate age and CNIC input, search for a registered voter, view all registered voters, view basic voting requirements, and repeatedly interact with the program through a menu.

This project is designed as a beginner-level Python practice project for learning:

Functions
User input
Conditional statements
if, elif, and else
while loops
Input validation
Exception handling with try and except
Integer conversion
String comparison
Lists
Dictionaries
Dictionary access
The in operator
enumerate()
Basic program flow
Features

The current version of the program includes:

Register to vote
Ask for the user's full name
Validate age input
Check voter eligibility based on age
Require voters to be 18 or older
Validate CNIC format
Store registered voters in a list
Store voter information using dictionaries
Display registration details
View a registered voter's details using their CNIC
View all registered voters
Display basic voting requirements
Validate menu choices
Continuously display the menu until the user chooses to exit
Display invalid input messages
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


The menu is inside a while True loop, so after completing an operation, the program returns to the menu until option 6 is selected.

Register to Vote

Select option 1 to register a voter.

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


The registration functionality is handled by the register_voter() function.

def register_voter():


The function collects the user's name and age.

If the user is 18 or older, the program asks for their CNIC. After successful CNIC validation, the voter information is stored in the voters list.

Each voter is stored as a dictionary:

voter = {
    "name": name,
    "age": age,
    "cnic": cnic
}


The dictionary is then added to the list:

voters.append(voter)

Voter Storage

Registered voters are stored in an in-memory list:

voters = []


Each registered voter is represented by a dictionary containing:

name
age
cnic


For example:

{
    "name": "Ali Ahmed",
    "age": 25,
    "cnic": "42101-1234567-1"
}


The information is only stored while the program is running. It is not saved to a file or database.

Age Validation

The program uses the get_valid_age() function to validate age input.

def get_valid_age():


The function repeatedly asks the user for their age and converts the input to an integer.

age = int(input("Please enter your age: "))


If the user enters something that cannot be converted to an integer, a ValueError is caught:

except ValueError:
    print("Invalid age. Please enter a valid number.")


The program then asks the user to enter the age again.

Example:

Please enter your age: abc
Invalid age. Please enter a valid number.
Please enter your age: 25

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

CNIC Validation

The program validates the CNIC using the get_valid_cnic() function:

def get_valid_cnic():


The required format is:

XXXXX-XXXXXXX-X


For example:

42101-1234567-1


The validation checks:

Total length is 15 characters
Character at position 6 is -
Character at position 14 is -
First 5 characters are digits
Middle 7 characters are digits
Final character is a digit

The validation logic is:

if (
    len(cnic) == 15
    and cnic[5] == '-'
    and cnic[13] == '-'
    and cnic[:5].isdigit()
    and cnic[6:13].isdigit()
    and cnic[14].isdigit()
):
    return cnic


If an invalid CNIC is entered, the program continues asking for a valid CNIC.

Example:

Please enter your CNIC: 12345
Invalid CNIC. Please use the format XXXXX-XXXXXXX-X.
Please enter your CNIC: 42101-1234567-1

Check Voter Eligibility

The project contains a check_voter_eligibility() function:

def check_voter_eligibility():


The function is designed to ask for the user's age and determine whether they are eligible to vote.

Its intended behavior is:

You have selected to check voter eligibility.
Please enter your age: 20
You are eligible to vote.


For someone under 18:

Please enter your age: 16
Sorry, you are not eligible to vote.
You must be 18 or older.


The function uses:

if age >= 18:
    print("You are eligible to vote.")
else:
    print("Sorry, you are not eligible to vote.")
    print("You must be 18 or older.")

Current Menu Issue

There is currently an issue in the main menu.

Option 2 is intended to call:

check_voter_eligibility()


However, the current code actually calls:

elif choice == '2':
    get_valid_cnic()


Therefore, selecting option 2 currently asks the user for a CNIC instead of checking voter eligibility.

To fix this, change:

elif choice == '2':
    get_valid_cnic()


to:

elif choice == '2':
    check_voter_eligibility()

View Voter Details

Select option 3 to view the details of a registered voter.

The program first checks whether any voters have been registered.

If there are no registered voters:

You have selected to view voter details.
No registered voters found.


If voters exist, the program asks for the voter's CNIC:

Please enter the CNIC of the voter:


The program searches the voters list and compares the entered CNIC with each voter's CNIC.

If a matching voter is found, their details are displayed:

Voter Details
Name: Ali Ahmed
Age: 25
CNIC: 42101-1234567-1


If no matching voter is found:

No voter found with this CNIC.


The functionality is implemented using:

def view_voter_details():

View All Registered Voters

Select option 4 to view all registered voters.

If there are no registered voters:

You have selected to view all registered voters.
No registered voters found.


If registered voters exist, the program displays each voter:

All Registered Voters:

Voter 1
Name: Ali Ahmed
Age: 25
CNIC: 42101-1234567-1

Voter 2
Name: Sara Khan
Age: 30
CNIC: 35202-7654321-2


The functionality is implemented using:

def view_all_registered_voters():


The program uses enumerate() to number the voters:

for number, voter in enumerate(voters, start=1):

Voting Requirements

Select option 5 to view the basic voting requirements.

The program displays:

You have selected to view voting requirements.
To be eligible to vote, you must:
- Be a citizen of the country
- Be at least 18 years old
- Register to vote before the election


This functionality is implemented in:

def show_voting_requirements():

Exit

Select option 6 to exit the program.

The program displays:

Exiting the program. Thank you for using the Voter Eligibility Checker!


The exit option uses break to stop the main while True loop:

elif choice == '6':
    print("Exiting the program. Thank you for using the Voter Eligibility Checker!")
    break

Menu Validation

The program validates menu selections using a while loop:

while choice not in ['1', '2', '3', '4', '5', '6']:
    print("Invalid choice. Please select a valid option (1-6).")
    choice = input("Please select an option (1-6): ")


This ensures that the program does not continue until the user enters one of the valid menu choices.

Program Flow

The program follows this general flow:

Create an empty voters list.
Display the welcome message and menu.
Ask the user to select an option.
Validate the menu selection.
Execute the corresponding function.
Return to the menu.
Continue until the user selects option 6.

The main menu is implemented using:

while True:


The menu options are handled using if and elif statements.

if choice == '1':
    register_voter()
elif choice == '2':
    get_valid_cnic()
elif choice == '3':
    view_voter_details()
elif choice == '4':
    view_all_registered_voters()
elif choice == '5':
    show_voting_requirements()
elif choice == '6':
    print("Exiting the program. Thank you for using the Voter Eligibility Checker!")
    break


Note: Option 2 currently contains the implementation issue described in the Check Voter Eligibility section.

Functions

The project currently contains the following functions:

Function	Purpose
get_valid_age()	Validates and returns a numeric age
register_voter()	Registers an eligible voter
check_voter_eligibility()	Checks whether a person is eligible to vote
get_valid_cnic()	Validates the CNIC format
view_voter_details()	Searches for and displays one registered voter
show_voting_requirements()	Displays voting requirements
view_all_registered_voters()	Displays all registered voters
Python Concepts Used

This project practices several Python fundamentals:

Functions
Function calls
if, elif, and else statements
while loops
for loops
try and except
ValueError handling
Membership checking with in
User input with input()
Integer conversion with int()
String comparison
String slicing
String methods such as isdigit()
Lists
Dictionaries
Dictionary keys and values
List methods such as append()
enumerate()
Conditional operators
return
break
Basic program flow
Current Limitations

Although the project now supports voter storage and searching, it still has some limitations:

Option 2 currently calls get_valid_cnic() instead of check_voter_eligibility().
Voter information is stored only in memory.
All voter information is lost when the program exits.
There is no database or file storage.
CNIC uniqueness is not checked, so the same CNIC could potentially be registered more than once.
Age input is checked for numeric values, but negative ages are not explicitly rejected.
Full name input is not validated.
CNIC validation checks the format but does not verify whether the CNIC actually belongs to a real person.
The program does not provide functionality for editing or deleting registered voters.
There is no separate search function; voter searching is currently performed through view_voter_details().
The voting requirements are basic informational requirements and may not represent the complete legal requirements of a specific country or election.
Future Improvements

Possible improvements include:

Fix option 2 so it calls check_voter_eligibility().
Prevent duplicate CNIC registrations.
Add validation to ensure age is a positive number.
Validate the user's name.
Add edit voter functionality.
Add delete voter functionality.
Add a dedicated voter search feature.
Save voter information to a file.
Use a database for persistent storage.
Add stronger CNIC validation.
Add better error handling.
Improve the terminal user interface.
Organize the project into multiple Python files as it grows.
Add unit tests for individual functions.
Add more detailed voting requirements based on the target country's election laws.
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


After registration, the program returns to the main menu because the menu is inside a continuous loop.

For example, the user can then select option 4:

Please select an option (1-6): 4
You have selected to view all registered voters.

All Registered Voters:

Voter 1
Name: Ali Ahmed
Age: 25
CNIC: 42101-1234567-1

Project Purpose

This project is primarily intended for Python practice and learning.

It demonstrates how basic Python concepts can be combined to create a simple interactive terminal application.

The project is useful for practicing:

User input
Functions
Conditional logic
Loops
Input validation
Exception handling
Lists
Dictionaries
Searching through data
Basic data storage
Program structure
License

This project is intended for educational and practice purposes.