__author__ = 'Atalay Samet Ergen'
"""
An emirp ("prime" spelled backwards) is a prime whose (base 10) reversal is also prime,
but which is not a palindromic prime. Similarly, A prime whose digital reverse is a different prime.
The first few are 13, 17, 31, 37, 71, 73, 79, 97, 107, 113, 149, 157, ... (OEIS A006567).
A binary plot of the emirps is illustrated above.
Reference: http://mathworld.wolfram.com/Emirp.html
"""


def isPrime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0 and number != 2:
                # not prime)
                break
        else:
            return True
    else:
        print("The integer must be greater than 1")

    return False


def reverseTheNum(theNum):
    r = 0
    while theNum > 0:
        r *= 10
        r += theNum % 10
        theNum //= 10
    return r


def countEmirpPrime(inputNumber):
    counter = 0
    for i in range(13, inputNumber + 1):
        if isPrime(i):
            x = reverseTheNum(i)
            if (x != i) and isPrime(x):
                counter += 1
                # print("numbers",i)
    return counter


print(countEmirpPrime(40))
