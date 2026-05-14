#user input add a key value and update teh values
d = {}
n = int(input("enter the numbers:"))
for i  in range(n):
    key  = input("enter the key values:")
    values = input("enter the values:")
    d[key] = values
key = input("enter the key to update:")
values = input("enter the new value:")    
d.update({key:values})
print(d) 

 #checkong whether teh key is exist un the dictioanry or not 
 #if there print exis t not their not fornd
d = {}
n =  int(input("enter the numbers"))
for i in range(n):
    key = input("enter the key values:")
    values = input("enter the values:")
    d[key] = values
key = input("enter the key to check:")
if key in d:
        print("exist")
else:
        print("not found:")            