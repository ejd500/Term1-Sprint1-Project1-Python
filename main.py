# Program description: Sprint # 1 - Project # 1
# Author: Ellen Dalton, Matthew Menchinton, Corina Jewer
# Date started: June 21, 2023
# Date finished: June 28, 2023

# Import any required libraries
import datetime
import random

# Define program constants.
DAILY_RATE = 85.00
MILEAGE_RATE_OWN_CAR = 0.17
MILEAGE_RATE_RENTED_CAR = 65.00
HST_RATE = 0.15

# Define a required functions.


def validate_first_name(emp_first_name):
    # Function to validate a person's first name.

    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        if emp_first_name == "":
            print("Error - employee's first name cannot be blank.")
            break
        elif not set(emp_first_name).issubset(allowed_char):
            print("Error - employee's first name contains invalid characters.")
            break
        else:
            return emp_first_name


def calc_hst(claim_amt):
    # Function to calculate HST

    hst = claim_amt * HST_RATE
    return hst


def emp_travel_claim():
    # Function to process salesperson travel claims.
    # Option 1

    # Inputs
    while True:
        while True:
            emp_num = input("Enter the employee number: ")
            if emp_num == "":
                print("Error - Employee number must be entered.")
            elif len(emp_num) != 5:
                print("Error - Employee number must be 5 digits.")
            elif not emp_num.isdigit():
                print("Error - Employee number must be 5 digits.")
            else:
                break

        while True:
            first_name = input("Enter the employee's first name: ").title()
            if validate_first_name(first_name):
                break

        while True:
            allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
            emp_last_name = input("Enter the employee's last name: ").title()
            if emp_last_name == "":
                print("Error - employee's last name cannot be blank.")
            elif not set(emp_last_name).issubset(allowed_char):
                print("Error - employee's last name contains invalid characters.")
            else:
                break

        location = input("Enter the location of the trip: ").title()

        while True:
            allowed_char = set("0123456789-")
            start_date = input("Enter the start date of the trip (YYYY-MM-DD): ")
            if start_date == "":
                print("Error - start date cannot be blank.")
            elif len(start_date) != 10:
                print("Error - start date must be 10 characters long, in the YYYY-MM-DD format.")
            elif not set(start_date).issubset(allowed_char):
                print("Error - start date contains invalid characters.")
            elif start_date[4] != "-" and start_date[7] != "-":
                print("Error - start date must be in the YYYY-MM-DD format.")
            elif not start_date[0:4].isdigit() and start_date[5:7].isdigit() and start_date[8:10].isdigit():
                print("Error - start date must be in the YYYY-MM-DD format.")
            else:
                start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
                break

        while True:
            allowed_char = set("0123456789-")
            end_date = input("Enter the end date of the trip (YYYY-MM-DD): ")
            if end_date == "":
                print("Error - end date cannot be blank.")
            elif len(end_date) != 10:
                print("Error - end date must be 10 characters long, in the YYYY-MM-DD format.")
            elif not set(end_date).issubset(allowed_char):
                print("Error - end date contains invalid characters.")
            elif end_date[4] != "-" and end_date[7] != "-":
                print("Error - end date must be in the YYYY-MM-DD format.")
            elif not end_date[0:4].isdigit() and end_date[5:7].isdigit() and end_date[8:10].isdigit():
                print("Error - end date must be in the YYYY-MM-DD format.")
            else:
                end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
                if end_date <= start_date:
                    print("Error - end date must be later than start date.")
                elif end_date > start_date + datetime.timedelta(days=7):
                    print("Error - end date must be no more than 7 days after the start date.")
                else:
                    break

        num_days = (end_date - start_date).days

        while True:
            allowed_char = set("OR")
            car_used = input("Enter the type of car you used (O for own car or R for rental): ").upper()
            if car_used == "":
                print("Error - Type of car used cannot be blank")
            elif len(car_used) != 1:
                print("Error - Type of car used must be O or R only.")
            elif not set(car_used).issubset(allowed_char):
                print("Error - Type of car used must be O or R only.")
            else:
                break

        while True:
            if car_used == "O":
                try:
                    tot_km_travelled = float(input("Enter the total kilometers travelled: "))
                except:
                    print("Error - Total KM's travelled is not a valid number. Please re-enter.")
                else:
                    if tot_km_travelled > 2000.00:
                        print("Error - Total KM's travelled cannot exceed 2000.00")
                    else:
                        break
            if car_used == "R":
                break

        while True:
            allowed_char = set("SE")
            claim_type = input("Enter the claim type as standard or executive (S or E): ").upper()
            if claim_type == "":
                print("Error - claim type cannot be blank.")
            elif len(claim_type) != 1:
                print("Error - claim type must be S or E only.")
            elif not set(claim_type).issubset(allowed_char):
                print("Error - Type of car used must be S or E only.")
            else:
                break

        # Calculations

        per_diem_amt = num_days*DAILY_RATE

        if car_used == "O":
            mileage_amt = MILEAGE_RATE_OWN_CAR * tot_km_travelled

        if car_used == "R":
            mileage_amt = MILEAGE_RATE_RENTED_CAR * num_days

        bonus = 0

        if num_days > 3:
            bonus = bonus + 100.00

        if car_used == "O" and tot_km_travelled > 1000:
            bonus = bonus + 0.04*tot_km_travelled

        if claim_type == "E":
            bonus = bonus + 45.00*num_days

        if datetime.datetime(2023, 12, 15) <= start_date <= datetime.datetime(2023, 12, 22):
            bonus = bonus + 50.00*num_days

        claim_amt = per_diem_amt + mileage_amt + bonus

        hst = calc_hst(claim_amt)

        claim_total = claim_amt + hst

        # Output
        print()
        print("Employee Travel Claim Information")
        print()
        print(f"Employee Number:        {emp_num}")
        print(f"Employee First Name:    {first_name}")
        print(f"Employee Last Name:     {emp_last_name}")
        print(f"Location of the Trip:   {location}")
        start_date_dsp = start_date.strftime("%B %d, %Y")
        print(f"Start Date:             {start_date_dsp}")
        end_date_dsp = end_date.strftime("%B %d, %Y")
        print(f"End Date:               {end_date_dsp}")
        print(f"The Number of Days:     {num_days} days")
        print()
        print(f"Claim Type (standard or executive): {claim_type}")
        print(f"Type of Car Used (own or rental):   {car_used}")
        if car_used == "O":
            print(f"Total KM's Travelled:        {tot_km_travelled:>8,.2f}")
        print()
        print(f"Per-Diem Amount:    ${per_diem_amt:>8,.2f}")
        print(f"Mileage Amount:     ${mileage_amt:>8,.2f}")
        print(f"Bonus:              ${bonus:>8,.2f}")
        print(f"Claim Amount:       ${claim_amt:>8,.2f}")
        print(f"HST:                ${hst:>8,.2f}")
        print(f"Claim Total:        ${claim_total:>8,.2f}")
        print()
        while True:
            allowed_char = set("YN")
            Continue = input("Do you want to continue (Y/N)? ").upper()
            if Continue == "":
                print("Error - you must enter Y or N.")
            elif len(Continue) != 1:
                print("Error - you must enter Y or N onlu.")
            elif not set(Continue).issubset(allowed_char):
                print("Error - you must enter Y or N only")
            else:
                break
        if Continue == "N":
            break


def interview_question():
    # Function for FizzBizz problem
    # Option 2

    while True:
        for num in range(1, 101):
            if num % 5 == 0 and num % 8 == 0:
                print("FizzBizz", end="")
                print()
            elif num % 5 == 0:
                print("Fizz", end="")
                print()
            elif num % 8 == 0:
                print("Bizz", end="")
                print()
            else:
                print(num)

        Continue = input("Press Enter key to run again, or enter 'Q' to quit: ").upper()
        if Continue == "":
            continue
        elif Continue == "Q":
            break


def strings_and_dates():
    # Function for cool stuff with strings and dates.
    # Option 3

    while True:
        # Employee information
        first_name = input("Enter employee's first name: ").title()
        last_name = input("Enter employee's last name: ").title()
        phone_number = input("Enter employee's phone number (###-###-####): ")
        start_date_str = input("Enter employee's start date (YYYY-MM-DD): ")
        birth_date_str = input("Enter employee's birthdate (YYYY-MM-DD): ")

        # Convert start date and birthdate strings to datetime objects
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()

        # Current date
        current_date = datetime.date.today()

        # Concatenate employee's full name
        full_name = first_name + " " + last_name
        print("Employee Name:", full_name)

        # Extract the area code from the phone number
        area_code = phone_number[:3]
        print("Area Code:", area_code)

        # Calculate the number of days between start date and current date
        days_employed = (current_date - start_date).days
        print("Days Employed:", days_employed)

        # Calculate the employee's age based on the birthdate
        age = (current_date - birth_date) // datetime.timedelta(days=365.25)
        print("Age:", age)

        choice = input("Enter 'Q' to quit, or any other key to continue: ").upper()
        if choice == "Q":
            break


def check_guess():
    # This program is the "You Already Guessed That Number" game with the use of a list.
    # Option 4: Something Old, Something New

    while True:
        number = random.randint(1, 51)
        previous_guesses = []  # Creating an empty list of the previously guessed numbers.
        num_guess = 0
        print("Welcome to the 'You Already Guessed That Number' Game!")
        print("Choose a number between 1 and 50.")

        while True:

            while True:
                try:
                    guess = int(input("Take your best guess: "))
                except:
                    print("Number is not a valid number - please re-enter.")
                else:
                    if guess < 0 or guess > 50:
                        print("Number must be between 0 and 50 - please re-enter.")
                    else:
                        break

            if guess in previous_guesses:
                print("You already guessed that number. Try again!")
                print("Your guesses: ", previous_guesses)  # Calling on the list.
                continue

            previous_guesses.append(guess)  # Using the append method to add a single item to the end of the list.

            num_guess = num_guess + 1

            if num_guess >= 5:
                print(f"Sorry, you used {num_guess} guesses. You Lose!")
                break

            if guess < 0 or guess > 50:
                print("You must enter a number between 1 and 50. Try again!")
            elif guess < number:
                print("Your guess is too low! Try again.")
            elif guess > number:
                print("Your guess is too high! Try again.")
            else:
                print("Congratulations! You guessed the number!")
                break

        continue_game = input("Press any key to play again or enter 'Q' to quit: ").upper()
        if continue_game != "Q":
            check_guess()
        else:
            print()
            print("That's all for now folks.")
            # In this example, I used the syntax to crete a new list without any pre-assigned values.
            # new_list_name = [ ]  This is done with use of blank square brackets.
            # I then added the previously guessed numbers to the empty list by using the append() method.
            # This allowed me to create a list of previously guessed numbers and display this list to the
            # player in the event they entered a duplicate number and were unsure of their previous guesses.
            # Lists are ordered, the items have a defined order, and that order will not change.
            # If you add new items to a list using the append method, the new items will be placed at the end of the list.

            # To insert a list item at a specified index, use the insert() method. Lists are mutable
            print()
            print("Please see some more examples of modifying, appending, removing and inserting items in a list:")
            print()
            groceries = ["apples", "chocolate", "chips"]
            print(f"Original list:              {groceries}")

            groceries.insert(1, "oranges")  # This will place oranges in index 1 position which will be immediately after apples.
            print(f"Modified List 1:            {groceries}")

            groceries[0] = "kiwi"  # Modifying an item, this will change apples to kiwi.
            print(f"Modified List 2:            {groceries}")

            groceries.append("grape")  # Adding an item, this will add grape at the end of the list as it did in the guess game.
            print(f"Appending an item:          {groceries}")

            groceries.remove("chocolate")  # Removing an item, this will remove chocolate from the list.
            print(f"Removing an item:           {groceries}")

            print(f"Accessing an item by index: {groceries[2]}")  # Accessing an item by index, this will print chips.
            print(f"Ammended list:              {groceries}")  # This will print our amended list.
            print()
            print()
            break

# Main program.

while True:
    print()
    print("NL Chocolate Company")
    print("Travel Claims Processing System")
    print()
    print("1. Enter an Employee Travel Claim")
    print("2. Fun Interview Question")
    print("3. Cool Stuff with Strings and Dates")
    print("4. Something Old, Something New")
    print("5. Quit Program")
    print()
    while True:
        try:
            Choice = int(input("   Enter choice (1-5): "))
        except:
            print("Error - choice is not a valid entry.")
        else:
            if Choice < 1 or Choice > 5:
                print("Error - Choice must be between 1 and 5.")
            else:
                break
    if Choice == 1:
        emp_travel_claim()
    elif Choice == 2:
        interview_question()
    elif Choice == 3:
        strings_and_dates()
    elif Choice == 4:
        check_guess()
    else:
        break

# Housekeeping
print()
print("Thanks for using NL Chocolate Company's Travel Claims System")
print("Come again soon.")
print()
