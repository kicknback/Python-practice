new_string = "blah blah blah"
copied_str = new_string[:]
# print(copied_str)


# Tiny car program

input(">")
print('''
    The car game
    Start > Starts the car
    Stop > Stops the car
    Quit > Exits the program''')

while True:
    user_input = input(">").lower()
    if user_input == "start":
        print("Car has started!...")
    elif user_input == "stop":
        print("Car has stopped.")
    elif user_input == "quit":
        print("Exiting program...")
        break
    else:
        print("I don't understand that command")


