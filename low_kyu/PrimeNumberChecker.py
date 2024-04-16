# function will check if argument passed is a prime number
def prime_checker(num):
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


print(prime_checker(-1))
