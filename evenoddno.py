numbers=(21,3,5,2,8,7)
count_odd=0
count_even=0
for x in numbers:
    if not x % 2 :
        count_odd += 1
        
    else:
        count_even += 1
        
        print("Number of even numbers  :",count_even)
        print("Number of odd number :",count_odd)