def check_palindrome(n):
    return str(n) == str(n)[::-1]

palindromes=[]
x=True
for i in range(999,1,-1):
    for j in range(999,1,-1):
        if check_palindrome(i*j):
            palindromes.append(i*j)
            break
    
print(max(palindromes))



