voters = []
def get_valid_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            return age
        except ValueError:
            print("Invalid age. Please enter a valid number.")

def register_voter():
    print("You have selected to register to vote.")

    name = input("Please enter your full name: ")
    age = get_valid_age()

    if age >= 18:
        print("You are eligible to register.")
        cnic = input("Please enter your CNIC: ")

        voter = {
            "name": name,
            "age": age,
            "cnic": cnic
        }

        voters.append(voter)

        print("\nRegistration Successful!")
        print("Name:", name)
        print("Age:", age)
        print("CNIC:", cnic)

    else:
        print("Sorry, you are not eligible to register.")
        print("You must be 18 or older.")
def view_all_registered_voters():
    print("You have selected to view all registered voters.")

    if not voters:
        print("No registered voters found.")
        return

    print("\nAll Registered Voters:")

    for number, voter in enumerate(voters, start=1):
        print(f"\nVoter {number}")
        print("Name:", voter["name"])
        print("Age:", voter["age"])
        print("CNIC:", voter["cnic"])


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

    age = int(input("Please enter your age: "))

    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("Sorry, you are not eligible to vote.")
        print("You must be 18 or older.")

elif choice == '4':
    view_all_registered_voters()

elif choice == '5':
    print("You have selected to view voting requirements.")
    print("To be eligible to vote, you must:")
    print("- Be a citizen of the country")
    print("- Be at least 18 years old")
    print("- Register to vote before the election")
elif choice == '6':
    print("Exiting the program. Thank you for using the Voter Eligibility Checker!")