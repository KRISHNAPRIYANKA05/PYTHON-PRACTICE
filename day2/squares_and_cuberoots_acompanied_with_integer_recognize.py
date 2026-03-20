#today we are going to write the code for 2 programs in this that includes calucylaing the quareroot and cuberoot and printing whwther the given number is positve or negative or zer

num = int(input("enter the number:"))
square_root = num**2
print ("the suare root of the given number is:",square_root)
cube_root = num**3
print("the cube root of teh gven number is :",cube_root)

#printing thecategory of the number 
if num>0:
    print("the number is postive")
elif num<0:
    print("the number is negative")
else:
    print("the number is 0")        