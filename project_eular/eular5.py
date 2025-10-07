number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(2520,3000000000,20):
    divided_remainder=list(map(lambda x: i%x,number_list))
    if divided_remainder==[0]*20:
        print(i)
        break   