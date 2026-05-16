"""function: it is a  block of reusable code that performs specific 
code and perfromaece specific task.
key points:
helps avoid repititon of the code 
improves modularity(breaking large code in to smaller code)
can accept input()parameter nd retutn output"""

"""calling:
declarartion:
def function_name(parameters):
    code can be executed.
return value    
arguements """

#example of function
def add(a,b):
    return a+b
result = add(100,200)
print(result)

#square od a number by the function
def square(num):
    return num**2
result  = square(int(input("Enter the number: ")))
print(result)

"""built - in functions: print(), input(), int(), float(), str(), len(), range(),lambda()
lambda:A lambda function is a small anonymous function in Python.
Anonymous means it has no name.
It is usually used for short, simple operations.
syntax:lambda arguments:expression"""

#no arguments and no return value
def greet():
    print("hello")
greet()

#arguments but no retun values
def greet(name):
    print(name)
greet("alice")   


#no arguments but return values
def msg():
    return"Hello, World!"
x = msg()
print(x)

#arguments and return values
def may(a,b):
    return a*b
k =may(6,7)
print(k)  

"""the main differnces between  print and retun()is
that print() only dipalys the output where as the 
retun only gives the specified  value in the function

types of  arguments:
positional: specifying the position to the varaible here oreder matters
varaible:declaring the varaible number of arguments
default:assigning the values in the parameters of teh fumnction
keyword:"""

#varaible argument passing

def st(name,age):
    print(name,age)
st(name = "priyanka",age = 21)   

#default arguments
def name(n = "priyanka"):
    print(n)
name("revathi")    
