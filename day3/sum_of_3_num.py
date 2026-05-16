""" In this program we are going to write the program
for finding the sum of 3 numbers in both the 
global variabes and  local variables."""

#global variable declaration
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the valuse of c:"))

def sum(a,b,c):
    return(a+b+c)
print("the sum of 3 numbers is:",sum(a,b,c))

#local variables
def add(p,q,r):
    return(p+q+r)
print("the sum of 3 numbers is:",add(12,45,65))
