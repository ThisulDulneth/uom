#function for checking prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#getting the prime numbers into a list
x= True
n=2
prime_numbers = []  
while x:
    if is_prime(n):
        prime_numbers.append(n)
    if len(prime_numbers) == 10001:
        print(prime_numbers[-1]) #printing the 10001st prime number in the list
        x=False
    n+=1
