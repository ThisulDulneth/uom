#Largest prime factor of 600851475143

def check_prime(n):     # function for checking the prime numbers
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def getting_factors(n):   # function for getting the factors of the number
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return factors

def getting_prime_factors(factors):   # function for getting the prime factors from the factors
    prime_factors = []
    for factor in factors:
        if check_prime(factor):
            prime_factors.append(factor)
    return prime_factors

prime_fac_list=getting_prime_factors(getting_factors(600851475143))
print(max(prime_fac_list))   # printing the largest prime factor from the list of prime factors


