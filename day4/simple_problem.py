 #GENRATE AND PRINT A DICTIOANASY TAT CONTAINS A  NUMBER (x:x*x)format
d ={}
n = int(input("enter the number:"))
for i in range(1,n+1):
     d[i] = i*i
print(d) 

#merging 2 dictionaries
d ={}
d1 = {}
d2 = {}
n1 = int(input("enter the number of elements in the dictioanr:"))
for i in range(n1):
    key1 = input("enter the key values:")
    values1  = input("enter the values:")
    d1[key1] = values1
n2 = int(input("enter the number of elements in the dictioanry:"))
for i in range(n2):
    key2 = input("enter teh keys")
    value2 = input("enter teh values")
    d2[key2]=value2   
d2 = d.copy()    
d1.update(d2)
print(d1)     

# delete an element
q = {}
n = int(input("enter the number of elements: "))
for i in range(n):
    k = input("enter the key: ")
    v = input("enter the value: ")
    q[k] = v
print("Original dictionary:", q)

p = input("enter the key to delete: ")
if p in q:
    q.pop(p)
    print("Updated dictionary:", q)
else:
    print(f"Key '{p}' not found in the dictionary.")
