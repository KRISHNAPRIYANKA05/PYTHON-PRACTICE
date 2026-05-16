"""practice programs"""

#reversing the string
h = input("enter the word:")
print(h[::-1])

#count the vowels in the sentence by function
k = input("enter the sentence")
def count_alphabets():
    vowels_count = 0
    consonant_count =0
    for i in k:
        if i.isalpha and i in "aeiouAEIOU":
           vowels_count+=1
        elif i.isalpha:
            consonant_count+=1   
    print(consonant_count,vowels_count)
count_alphabets()            

#palindrome word checking
p = input("enter the word:") #can also write 
h = p[::-1]
if p==h:
    print("palindrome")
else:
    print("not palindrome")

#counting the upper and lower
l = input("enter the string:")
count_upper =0
count_lower=0
for i in l:
    if i in i.upper():
        count_upper+=1
    elif i in i.lower():
        count_lower+=1
print(count_upper,count_lower)      

#removing the spaces
f = input("enter the sentence:")
print(f.replace(" ",""))



