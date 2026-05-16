""" in this program we are going to write the code for finding
whether the given number is even or not in 
both local and global variable."""

#global variable decalaration
a = int(input("enter the value of a:"))
def tine(a):
    if a>0:
        print("positive")
    elif a<0:
        print("negative")
    else:
        print("Zero")
    return a    
print("the given value a is:", tine(a))    

#local variable
def tine(ar):
    if ar>0:
        print("positive")
    elif ar<0:
        print("negative")
    else:
        print("Zero")
    return ar    
print("the given value a is:", tine(-89))    