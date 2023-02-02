def greater_than_zero(n):
    if n > 0:
        message = "Greater than zero"
    else:
        message = "Not greater than zero"
    return message

def main():
    print( greater_than_zero(2) )
    print( greater_than_zero(0) )
    print( greater_than_zero(-32) )

main()