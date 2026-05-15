"""recursion:the function that call itself
local varaible:varaible that works only inside the function and only defined 
inside the function
global varaibles:the varaible decalred outside of teh function and can be
 used all over the program including the functions.
"""
# factirial
def factorial(n):
    if n==0:
        return 1
    else:
        return n *factorial(n-1)
print(factorial(5))

#user defined in functions
def name():
    name = input("enter the name: ")
    return name
print(name())

a = int(input())
b = int(input())
def add(a,b):
    return a+b
print(add(a,b))


#even or odd
def even (a):
    if a%2 ==0:
        print("even")
    else:
        print("odd")    
a  = int(input("enter the number:"))
even(a)

#global varaible
num = int(input("enter the number:"))
def odd(num):
    if num%2 == 0:
        print("even")
    else:
        print("odd")  
odd(num)    

#larger number in 2 numbers ,global varaible
a = int (input("enter the num:"))
b = int(input("enter num2:"))
def largest(a,b):
    if a>b:
        print("a is larger")
    else:
        print("b is larger")
largest(a,b)   

#local varaible
def large(a,b):
    if a>b:
        print("a is larger")
    else:
        print("b is larger")
a = int(input("num1:"))        
b = int(input("num2:"))
large(a,b)