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


print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
