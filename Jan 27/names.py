def greeting(first_name, last_name):
    greet = "Hey there, " + first_name + " " + last_name
    return greet

def count_character(first_name, last_name):
    '''
    returns:
      intenger
    '''
    full_name = first_name + last_name
    character_count = len(full_name)
    return character_count

def calculate_year_born(age):
    year_born = 2023 - int(age)
    return year_born