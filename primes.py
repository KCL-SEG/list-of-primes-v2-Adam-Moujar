"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 2
    if number_of_primes <= 0:
        raise ValueError("Only positive numbers are allowed!")
    while(len(list) < number_of_primes):
        if checkIfPrime(count):
            list.append(count)
        count = count+1
    return list

def checkIfPrime(num):
    isPrime = True
    for i in range(2,num):
        if num != i and num % i == 0:
            isPrime = False
    return isPrime
