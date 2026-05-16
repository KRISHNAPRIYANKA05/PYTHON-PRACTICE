""" in this program we are gooing to write codde for largest in given two numbers and largest in given
three numbers """
#largest of two numbers
num1 = int(input("enter the first number:"))
num2 =  int(input("enter the second number:"))
if num1>num2:
    print("the largest number is :",num1)
else:
    print("the largest number is :",num2)

#finding largest numberin between 3 numbers
A = int(input("enter the value of A: "))
B = int(input("enter the value of B:"))
C = int(input("enterthe value of C:"))
if A>B and A>C:
    print("the largest number is :",A)
elif B>A and B>C:
    print("te largest number is:",B)
else:
    print("the largest number is:",C)    



