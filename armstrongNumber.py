__author__ = "Atalay Samet Ergen"
"""
Given a number x, determine whether the given number is Armstrong number or not. 
A positive integer of n digits is called an Armstrong number of order n 
(order is number of digits) if.

The idea is to first count number digits (or find order). 
Let the number of digits be n. For every digit r in input number x, compute r**n. 
If sum of all such values is equal to n, then return true, else false.

Reference: http://www.geeksforgeeks.org/program-for-armstrong-numbers/
"""


def isArmstrongNumber(inputNumber):
    number = inputNumber
    totalNumber = 0
    while number > 0:
        totalNumber += ((number % 10) ** (numberofDigits(inputNumber)))
        number = number // 10
    if totalNumber == inputNumber:
        return True
    else:
        return False


def numberofDigits(number):
    counter = 0
    while number > 0:
        number = number // 10
        counter += 1
    return counter
