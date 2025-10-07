#  getting the square difference

def square_difference(n):
    sum_of_squares = sum([i**2 for i in range(1, n+1)])
    square_of_sum =sum([i for i in range(1, n+1)])**2
    return square_of_sum - sum_of_squares

print(square_difference(100))

