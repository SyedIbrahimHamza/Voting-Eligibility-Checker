def register_voter():
    print("You have selected to register to vote.")

    name = input("Please enter your full name: ")
    age = int(input("Please enter your age: "))

    if age >= 18:
        print("You are eligible to register.")
        cnic = input("Please enter your CNIC: ")

        print("\nRegistration Successful!")
        print("Name:", name)
        print("Age:", age)
        print("CNIC:", cnic)

    else:
        print("Sorry, you are not eligible to register.")
        print("You must be 18 or older.")

print("Welcome to Voter Eligibility Checker!")
print("1. Register to vote")
print("2. Check voter eligibility")
print("3. View voter details")
print("4. View all registered voters")
print("5. Voting Requirements")
print("6. Exit")
choice = input("Please select an option (1-6): ")
while choice not in ['1', '2', '3', '4', '5', '6']:
    print("Invalid choice. Please select a valid option (1-6).")
    choice = input("Please select an option (1-6): ")
if choice == '1':
    register_voter()
elif choice == '2':
    print("You have selected to check voter eligibility.")
elif choice == '4':
    print("You have selected to view all registered voters.")
elif choice == '5':
    print("You have selected to view voting requirements.")
    print("To be eligible to vote, you must:")
    print("- Be a citizen of the country")
    print("- Be at least 18 years old")
    print("- Register to vote before the election")
elif choice == '6':
    print("Exiting the program. Thank you for using the Voter Eligibility Checker!")