#mappping two lists in  a dictioanary
"""d = {}
a = input("enter the first list:").split()
b = input("enter the second list:").split()
d = dict(zip(a,b))
print(d)"""

#two dictionaries adding values for common key values
d = {}
d1 = {}
d2 = {}
n = int(input("enter the numbers in 1:"))
for i in range(n):
    k = input()
    v = input()
    d1[k] = v
print(d1)
r = int(input("enter the numbersin 2:"))
for i in range (r):
    k1 = input()
    v1 = input()
    d2[k1] = v1
print(d2)
for k in d1:
    if k in d2:
        d[k] = int(d1[k]) + int(d2[k])
print(d)    

