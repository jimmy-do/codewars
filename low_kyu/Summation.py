# Write a program that finds the summation of every number from 1 to num. The number will always be a positive
# integer greater than 0. Your function only needs to return the result.

def summation(n):
    if n > 1:
        return n + summation(n - 1)
    return 1


print(summation(3))
