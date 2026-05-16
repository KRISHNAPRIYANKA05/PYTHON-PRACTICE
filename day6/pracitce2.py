"""counting the frequency of the character in a  sentence
h = input("enter the sentence:")
d ={}
count_character=0
for i in h:
    if i.isalpha():
        for j in h:
            if i==j:
                count_character+=1
        d[i]=count_character
print(d)

#option 2:
s = input()
d = {}
for i in s:
    d[i]=s.count
print(d)   

#to print first non repeting character
g = input("enter the string:")
for i in g:
    if g.count(i) ==1:
        print(i)
        break

#to check whether they are anagsrma or not
#anagram:any 2 words that consisite of same letters in differnet arrangement
k = input("enter the first string:")
h = input("enter the second string:")

if sorted(k)==sorted(h):
    print("anagram")
else:
    print("not anagram")

#count the character in a word
g = input()
h = g.split()
print(len(h))

#print max length of the words
g = input("enter the sentence:")
k = g.split()
print(max(k,key=len))

#string compression
s = input()
d = {}
for i in s:
    if i.isalpha():
        d[i]=s.count(i)
for i in d:
    print(f"{i} {d[i]}",end="")     """   

 #removing the characters
s= input()
r = ''
for i in s:
    if i not in r:
        r+=i
print(r)    



