# writing factorial for a number with out recursive
"""def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i      
    return fact
n =int(input("enter the number:"))    
print(factorial(n))

#sum of digits of a number
def sum_of_digits(n):
    sum = 0
    while n>0:
        d = n%10
        sum+=d
        n =n//10
    return sum
n = int(input("enter the number:"))    
print(sum_of_digits(n))

#laregetc number in the list 
num = list(map(int,input("enter the number").split()))
def largest (num):
    num.sort()
    max = num[0]
    for i in num:
        if i>max:
            max = i
    return max
print(largest(num))

#EASY FORMAT
num = list(map(int,input("enter the number").split()))
def largest (num):
    return max(num)
print(largest(num))

#LENGTH Of The last word in a sentence 
s = input("emter the setence:").split()
def length():
    return(len(s[-1]))
print(length())

#whether the number is primt or not 
num = int(input("enter the numeber:"))
def prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i ==0:
            count +=1
    if count ==2:    
            print("is  prime")    
    else:
         print(" not  prime")
         
print(prime(num))

#printout the number of consonants in  a  sentence
s = input("enter the sentence:").split()
def constant(s):
    count_cons =0
    for i in s:
        if i.isalpha() and i not in "aeiouAEIOU":
            count_cons +=1
    return count_cons(s)   
print(constant())     """

