#dictionary the type of datastructures that are used to store the data in pair that contains key
#and value -keys are the identifiersand values are the data that need to be stored 
d ={}
print(type(d))

#Accessing values in the dictionary
k = {1:'one','a':'eleven'}
print(k[1])
print(k['a'])

#accessing elements  using get method
print(k.get('a'))

j= int(input("enter the values of s:"))
print(k.get(j))

#loop
k = {1:'one','a':'eleven'}
for i in k:
    print(i, ":", k[i])
