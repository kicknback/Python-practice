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
import string


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
    sum_of_25s = 0
    sum_of_50s = 0
    for ticket in people:
        if ticket == 25:
            sum_of_25s += 1
        elif ticket == 50:
            if sum_of_25s == 0:
                return "NO"
            else:
                sum_of_50s += 1
                sum_of_25s -= 1
        else:
            if sum_of_50s == 0 and sum_of_25s == 0:
                return "NO"
            elif sum_of_50s == 1 and sum_of_25s == 0:
                return "NO"
            elif sum_of_50s == 0 and sum_of_25s >= 3:
                sum_of_25s -= 3
            elif sum_of_50s >= 1 and sum_of_25s >= 1:
                sum_of_50s -= 1
                sum_of_25s -= 1
            else:
                return "NO"
    return "YES"


# print(tickets([25, 25, 25, 100, 50, 25, 25, 50]))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous
# subsequence in an array or list of integers:
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]

# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
# If the list is made up of only negative numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum.
# Note that the empty list or array is also a valid sublist/subarray.


def max_sequence(int_arr):
    if len(int_arr) == 0:
        return 0
    if all(i < 0 for i in int_arr):
        return 0
    max_so_far = -100000000
    max_ending_here = 0

    for i, val in enumerate(int_arr):
        max_ending_here = max_ending_here + int_arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral
# representation of that integer.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
# any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is
# written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#
# Example:
#
# solution(1000) # should return 'M'


def thousands(num):
    if num == 1:
        return "M"
    elif num == 2:
        return "MM"
    elif num == 3:
        return "MMM"


def hundreds(num):
    if num == 9:
        return "CM"
    elif num == 8:
        return "DCCC"
    elif num == 7:
        return "DCC"
    elif num == 6:
        return "DC"
    elif num == 5:
        return "D"
    elif num == 4:
        return "CD"
    elif num == 3:
        return "CCC"
    elif num == 2:
        return "CC"
    elif num == 1:
        return "C"
    elif num == 0:
        return ""


def tens(num):
    if num == 9:
        return "XC"
    elif num == 8:
        return "LXXX"
    elif num == 7:
        return "LXX"
    elif num == 6:
        return "LX"
    elif num == 5:
        return "L"
    elif num == 4:
        return "XL"
    elif num == 3:
        return "XXX"
    elif num == 2:
        return "XX"
    elif num == 1:
        return "X"
    elif num == 0:
        return ""


def ones(num):
    if num == 9:
        return "IX"
    elif num == 8:
        return "VIII"
    elif num == 7:
        return "VII"
    elif num == 6:
        return "VI"
    elif num == 5:
        return "V"
    elif num == 4:
        return "IV"
    elif num == 3:
        return "III"
    elif num == 2:
        return "II"
    elif num == 1:
        return "I"
    elif num == 0:
        return ""


def solution(n):
    roman_string = ""
    num_arr = [int(x) for x in str(n)]
    places = len(num_arr)

    if places == 4:
        roman_string += thousands(num_arr[0])
        roman_string += hundreds(num_arr[1])
        roman_string += tens(num_arr[2])
        roman_string += ones(num_arr[3])
    elif places == 3:
        roman_string += hundreds(num_arr[0])
        roman_string += tens(num_arr[1])
        roman_string += ones(num_arr[2])
    elif places == 2:
        roman_string += tens(num_arr[0])
        roman_string += ones(num_arr[1])
    elif places == 1:
        roman_string += ones(num_arr[0])

    # I = 1
    # V = 5
    # X = 10
    # L = 50
    # C = 100
    # D = 500
    # M = 1000

    return roman_string


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a
# human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.


def make_readable(seconds):
    secs = 0
    mins = 0
    hrs = 0
    for i in range(1, seconds + 1):
        secs += 1
        if secs > 59:
            mins += 1
            secs = 0
        if mins > 59:
            hrs += 1
            mins = 0

    if secs < 10:
        secs = "0" + str(secs)
    if mins < 10:
        mins = "0" + str(mins)
    if hrs < 10:
        hrs = "0" + str(hrs)

    return "{}:{}:{}".format(hrs, mins, secs)


# print(make_readable(86399))
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# A format for expressing an ordered list of integers is to use a comma separated list of either
#
# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
# The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans
# at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
# in the range format.
#
# Example:
#
# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"

# def solution_(args):
#     range_string = ""
#
#     while len(args) > 0:
#         range_counter = 0
#         add_item = True
#         item = args.pop(0)
#         if args[0] == item + 1:
#             start_value = item
#             while args[0] == item + 1:
#                 item = args.pop(0)
#                 range_counter += 1
#                 if not any(args):
#                     break
#             if range_counter < 2:
#                 range_string += str(start_value) + ','
#                 range_string += str((start_value + 1)) + ','
#             else:
#                 range_string += "{}-{},".format(start_value, start_value + range_counter)
#             add_item = False
#         if add_item:
#             range_string += str(item) + ','
#     return range_string[:-1]


# print(solution_([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
# print(solution_([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))

def solution_(args):
    range_string = ""

    while len(args) > 0:
        range_counter = 0
        add_item = True
        item = args.pop(0)
        if args[0] == item + 1 or args[0] == item - 1:
            if args[0] == item + 1:
                item_positive = True
            else:
                item_positive = False
            start_value = item
            while args[0] == item + 1 or args[0] == item - 1:
                item = args.pop(0)
                range_counter += 1
                if not any(args):
                    break
            if range_counter < 2:
                range_string += str(start_value) + ','
                if item_positive:
                    range_string += str((start_value + 1)) + ','
                else:
                    range_string += str((start_value + 1)) + ','
            else:
                range_string += "{}-{},".format(start_value, start_value + range_counter)
            add_item = False
        if add_item:
            range_string += str(item) + ','
    return range_string[:-1]


print(solution_([-52, -49, -46, -44, -41, -39, -37 - -35, -32 - -30, -28, -25, -23, -21, -18, -15, -13, -11]))
