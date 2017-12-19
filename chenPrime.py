__author__ = 'Atalay Samet Ergen'
"""
Chen primes: A prime number p is called a Chen prime if p + 2 is either a prime or semiprime.
Reference: https://prime-numbers.info/list/first-100-chen-primes
"""


def isPrime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0 and number != 2:
                # not prime)
                return False
        else:
            return True
    else:
        print("The integer must be greater than 1")


def chenPrime(inputNumber):
    localNumber = inputNumber + 2

    for i in range(2, localNumber + 1):

        for j in range(2, localNumber + 1):
            if isPrime(i) and isPrime(j):
                if ((localNumber) == (i * j)):
                    return True
    return False


def isChenPrime(theNumber):
    if isPrime(theNumber) and isPrime(theNumber + 2):
        return True

    elif (isPrime(theNumber) and chenPrime(theNumber)):
        return True
    else:
        return False


def listTheChenPrimes(num):
    for i in range(2, num + 1):
        if isPrime(i) and isPrime(i + 2):
            print(i)
        elif (isPrime(i) and chenPrime(i)):
            print(i)

    return "Done"


print(listTheChenPrimes(100))
print(isChenPrime(88))
print(isChenPrime(89))
