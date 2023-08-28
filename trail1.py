def is_even(input):
    return input %2==0

list1=[1,4,2,9,0,10]
print(list(filter(is_even,list1)))