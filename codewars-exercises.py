# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#
# Note: If the number is a multiple of both 3 and 5, only count it once.
# Also, if a number is negative, return 0(for languages that do have them)


# def solution(number):
#     if number < 0:
#         return 0
#     total = 0
#     for i in range(number):
#         if i % 3 == 0 and i % 5 == 0:
#             total += i
#             continue
#         if i % 3 == 0 or i % 5 == 0:
#             total += i
#     return total
#
#
# print(solution(16))


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Create a function named divisors/Divisors that takes an integer n > 1
# and returns an array with all of the integer's divisors' \
# '(except for 1 and the number itself), from smallest to largest.
# If the number is prime return the string '(integer) is prime'

# def divisors(integer):
#     if integer == 1 or integer == 2 or integer == 3:
#         return f"{integer} is prime"
#     div_arr = []
#     for i in range(2, (integer // 2) + 1):
#         if integer % i == 0:
#             div_arr.append(i)
#     if len(div_arr) == 0:
#         return f"{integer} is prime"
#     return div_arr
#
#
# print(divisors(100))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


# print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# The new "Avengers" movie has just been released!
# There are a lot of people at the cinema box office standing in a huge line.
# Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
#
# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
#
# Can Vasya sell a ticket to every person and give change
# if he initially has no money and sells the tickets strictly in the order people queue?
#
# Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment.
# Otherwise return NO.
#
# Examples:
# tickets([25, 25, 50]) # => YES
# tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
# tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change
# (you can't make two bills of 25 from one of 50)

def tickets(people):
    total = 0
    for ticket in people:
        if ticket == 25:
            total += ticket
        else:
            change = ticket - 25
            if change > total:
                return "NO"
            else:
                total -= change
    return "YES"


print(tickets([25, 25, 50, 50, 100]))














