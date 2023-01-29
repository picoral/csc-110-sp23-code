from names import *

def main():
    # prompt the user to enter their first and last name
    first_name = input("What's your first name?\n")
    last_name = input("What's your last name?\n")

    # call greeting with first and last name variables
    message = greeting(first_name, last_name)
    print(message)

    # call count character and print message
    nchar = count_character(first_name, last_name)
    message = "Your full name has " + str(nchar) + " letters."
    print(message)

    # prompt user to enter their age
    age = input("What's your age?\n")
    age_int = int(age)

    # call calculate_year_born with user's age
    year = calculate_year_born(age_int)

    # print message
    message = "You were born approximately in year " + str(year) +  "."
    print(message)


main() 