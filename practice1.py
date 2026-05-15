#user have to give the sentences and have to count the 
#no .of lower and upper in the sentence 
s = input("enter the sentence")
def sentence(s):
    caps_count = 0
    small_count = 0
    for i in s:
        if i.isupper():
            caps_count += 1
        elif i.islower():
            small_count += 1
    return caps_count, small_count
print(sentence(s))


#frequency of characters in dictioanry
s = input("enter the word:")
def frequency(s):
    from collections import Counter
    d=Counter(s)
    print(d)
print(frequency(s))   

#user will give u a randon list ,and printing out the second laregect number
a = list(map(int,input("enter the numbers").split()))
def second_largest(a):
    a.sort()
    a.remove(max(a))
print(a)
second_largest(a)


#reverse the number
n= int(input())
def reverse_number(n):
    if n==0:
        return
    else:
        print(n,end="")
        reverse_number(n-1)     
reverse_number(n)    