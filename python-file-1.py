new_string = "blah blah blah"
copied_str = new_string[:]
# print(copied_str)

# ############## Coding with Mosh ########################

# Tiny car program

# start = False
# stop = True
#
# while True:
#
#     user_input = input(">").lower()
#     if user_input == "start":
#         if start == True:
#             print("The car is already started.")
#         else:
#             print("Car has started!...")
#             start = True
#             stop = False
#     elif user_input == "stop":
#         if stop == True:
#             print("The car has already been stopped.")
#         else:
#             print("Car has stopped.")
#             stop = True
#             start = False
#     elif user_input == "quit":
#         print("Exiting program...")
#         break
#     elif user_input == "help":
#         print('''
#         The car game\n\nStart > Starts the car\nStop > Stops the car\nQuit > Exits the program
#         ''')
#     else:
#         print("I don't understand that command")


prices = [23, 435, 23, 82, 74, 283, 483, 134]
total = 0
for i in prices:
    total += i

# print(total)

# nested for loop to print letters in the output
numbers = [1, 1, 1, 1, 6]   #L
numbers = [5, 2, 5, 2, 2]   #F

# for i in numbers:
#     output = ''
#     for y in range(i):
#         output += 'x'
#     print(output)


# lists

# exercise to find highest number in a list

num_list = [3, 5, 25, 82, 32, 7, 13, 59, 21]

high_num = 0
for num in num_list:
    if num > high_num:
        high_num = num
# print(high_num)

# matricies

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix[1][2])

# remove duplicates in a list

dupe_list = [2, 4, 2, 6, 11, 4, 6, 5, 6, 7]
for i in dupe_list:
    if dupe_list.count(i) > 1:
        dupe_list.remove(i)
# print(dupe_list)

# dictionary ================================
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
# print(customer["name"])
# print(customer.get("name"))
# print(customer)

digits = {
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four "
}

# user_input = input("Phone: ")

# out_str = ""
#
# for ch in user_input:
#     out_str += digits.get(ch, "!")
# print(out_str)

# ========================== Functions ==============================

def square(num):
    return num * num


# print(square(18))

message = input(">")

def emoji_generator(msg):
    words = msg.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😢"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emoji_generator(message))







