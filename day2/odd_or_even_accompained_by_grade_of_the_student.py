 #In this programwe willcheck whether the given numberi is even or odd and also write code 
#define the grade of the student by marks system

#even or odd program
num = int(input("enter the number:"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")

#gradeing of the studentsby marks
marks = int(input("enter the maarks of the"))
if marks>90:
    print("first grade")
elif marks>=80   and marks<=90:
    print("second grade")
elif marks>=60 and marks<=80:
    print("third grade")
else:
    print("fail")    

