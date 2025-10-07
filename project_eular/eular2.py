# sum of the fibonacci even numbers 
t1=1
t2=2
fibonacci_list=[1]

#getting the fibonacci list using a whle loop
while t2<4000000:
    fibonacci_list.append(t2)
    t3=t1+t2
    t1=t2
    t2=t3

#deleting the odd numbers from the fibonacci list
fibonacci_list=list(filter(lambda x:x%2==0,fibonacci_list))

#getting sum of the fibonacci even numbers
sum_of_fibonacci_even_numbers=sum(fibonacci_list)
print(sum_of_fibonacci_even_numbers)


