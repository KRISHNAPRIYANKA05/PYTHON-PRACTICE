"""In this program i am going to 3 programs of diifernt types by 
declaring global and local variables in
 different cases for better understanding of the concept"""

#global varible by square claluculation
s = int(input("enter the value of s:"))
def square(s):
    return (s*s)
print(square(s))
#local variable
def Square(q):
    return(q*q)
print(Square(89))

#gobal decalration of p ,t,r
p = int(input("enter the value of p:"))
t = int(input("enter the value of t:"))
r = int(input("enter the value of r:"))
def s_i(p,t,r):
    return(p*t*r/100)
print("the simple interest is:", s_i(p,t,r))

#local variable declaration of p,t,r
def s_i(p,t,r):
    return(p*t*r/100)
print("the simple interest is:", s_i(4589666,2,13))

#global variable decalration of two numbers in between greatest
num1 = int(input("enter the num1 value"))
num2 = int(input("enterthe num2 value"))
def greatest(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
print("the greatest number is:", greatest(num1,num2))


#local varuiabls for largest
def greatest(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

print("the greatest number is:", greatest(78,456))
