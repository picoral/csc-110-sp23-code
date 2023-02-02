def say_hello(name):
  if name == "Bond" or name == "James Bond":
    print("Welcome on board 007.")
  else:
    print("Hello, " + name)

def main():
  user_name = input("Enter your name:\n")
  say_hello(user_name)

main()