from functools import reduce

def ty(num1,num2):
    return num1+num2

list1=[9,2,43,3]
print(reduce(ty,list1))