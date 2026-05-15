"""fibonaciseries:the series in which adding the first 2 numbers resulting the 
next succicent number
#simple form
num = int(input("enter the number:"))
def fibo(num):
    a,b= 0,1
    for i in range(num):
        print(a,end ="")
        a,b=b,a+b
fibo(num)        

#sortinf the elements without sort fumction
def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
        return lst  
lst = list(map(int,input("enter the numbers:").split()))
print(sort_list(lst))"""

#reversing a  string with recursion
str = input("enter the string:")
def reverse_string(str):
    for i in str:
        for j in str:
            return str [::-1]
            print(str)
reverse_string(str)
