# operations  in dictionary 
#modification AND ADDING  in dictionary 
k = {1: 'one', 's': 'seven',123 :"onetwenty three"}
k[1]="ONE"
k[3]="three"
print(k)

#by ising temp varaible - to swap the value 
dict1 = {'name':'john','age': 23}
temp = dict1.get("job")
print(temp)         

#update method- to upadate the value 
dict1.update({"job": "developer",'name':'priyanka'})
print(dict1)

#pop():  to remove nad and return an aelement from the doctionary 
dict1.pop("name")
print(dict1)

#popitem(): to remove and return an arbitrary key-value pair from the dictionary and
# # return it as tuple(last value)
dict1.popitem()
print(dict1)

#clear():remove all  the elements in the dictionary
dict1.clear()
print(dict1)

#key ():list of all key vaues in the dictionar
print(k.keys())

#values():list of alla values in the dictionary 
print(k.values())

#items():lis of all the keys and values pair in the dictionary 
print(k.items())

