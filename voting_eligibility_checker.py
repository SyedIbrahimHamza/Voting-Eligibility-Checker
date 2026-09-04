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
    print("You have selected to register to vote.")
    