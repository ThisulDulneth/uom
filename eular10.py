def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes_below(limit):
    total = 0
    for num in range(2, limit):
        if check_prime(num):
            total += num
    return total

print(sum_of_primes_below(2000000))# Problem 10: Summation of primes
# Find the sum of all the primes below two