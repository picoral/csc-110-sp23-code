def age_milestones(age):
    message = ""

    if age >= 18:
        message += "You may apply to join the military"

    if age >= 21:
        message += "You may drink"

    if age >= 35:
        message += "You might run for president"
    
    return message

def main():
    print( age_milestones(36))

main()