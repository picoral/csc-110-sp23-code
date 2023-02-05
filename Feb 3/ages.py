def age_milestones(age):
    message = ""

    if age < 16:
        message = "You have no responsibilities, enjoy!" 

    if age >= 16:
        message += "You may drive\n"

    if age >= 18:
        message += "You may apply to join the military\n"

    if age >= 21:
        message += "You may drink\n"

    if age >= 35:
        message += "You may run for president"

    return message

def validate_age(age):
    if age.isnumeric() == True:
        age = int(age)
        if 0 <= age <= 110:
            return True
    return False


def main():
    age = input("What's your age?\n")
    if validate_age(age) == True:
        age = int(age)
        print( age_milestones(age) )
    else:
        print("Please enter a valid age next time.")


main()