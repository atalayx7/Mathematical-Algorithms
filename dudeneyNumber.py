__author__ = "Atalay Samet Ergen"
"""
Reference Wikipedia: A Dudeney number is a positive integer that is a perfect cube such that 
the sum of its decimal digits is equal to the cube root of the number.
For example:

512=(5+1+2)^3

4913=(4+9+1+3)^3

19683=(1+9+6+8+3)^3
Write a function that returns true if a number is a Dudeney number and false otherwise.
"""


def isDudeneyNumber(inputNumber):
    number = inputNumber
    totalNumber = 0
    while number > 0:
        totalNumber += (number % 10)
        number = number // 10
    if totalNumber ** 3 == inputNumber:
        return True
    else:
        return False
