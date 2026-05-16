# tp print the largest the palindrom in the sentence
s = input().split()
w=[]
for i in s:
    if i[::-1]== i:
        w.append(i)
print(max(w,key=len))
    
    #panagram
s = input().split()
print(" ".join(s[::-1]))

