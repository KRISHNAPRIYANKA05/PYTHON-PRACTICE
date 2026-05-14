#convert a list into nested dictioanary of keys 
"""d ={}
k = list(map(int(input("enter the elements:").split())))

for i in range(k): 
    d = {i:k}
print(d)    
"""
#progrm to rint,items,keys,values
d ={}
n = int(input("enter the number of elements:"))
for i in range(n):
    k = input("enter the key:")
    v = input("enter the value:")
    d[k] = v
print("Items:", list(d.items()))
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))