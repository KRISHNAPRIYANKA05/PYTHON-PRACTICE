"""isalpha(): this is specifically used to find whether
 the given character is in alphabets.
 isdigit(): used to check whether the they are digits or not.
 isalnum():used to check alphabets ,numerical and special characters.
 strings  can also be declared inside the built n function in quotes
 startwith():checks the starting number
 endswith():checkes the ending number
 find():to check whether this exist ooor not if not theri it returns -1
 index():retuns the place value in the string.
 count():to coujnt the position of the words.
 split():to split t he sentences 
 strip(): it remves the spaces the the sentences
 rstrip():it removes teh space in the right side 
 lstrip():it removes the soace on the left side of teh sentences
 repalce(existing,new): to replace the words or  letter
"""
#checking the methods
m = "b"
print(m.isalpha())

k = "8"
print(k.isdigit())

print("cvx124".isalnum())

#start and end
v = "andhrapradesh"
#print(v.startswith("A"))
#print(v.endswith("pradesh"))
print(v.find("r"))
print(v.index("p"))
print(v.count("n"))

#using functions
k = " heelo worls, this is csm"
print(k.split(","))
print(k.strip())
print(k.rstrip())
print(k.lstrip())

#replace function
h = "hello world"
print(h.replace("e","z"))
j = "good" ,"morning"
print(" ".join(j))