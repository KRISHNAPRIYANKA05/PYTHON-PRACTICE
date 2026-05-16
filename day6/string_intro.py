"""strings:set of charaters that are enclosed by the coutes
 they can contain character ,special character and numericals
""
''
''' '''
strings are immutable because they dont indexing values
strings have indexing and it is called slicing
"""
#basic program
a = "hi priyanka"
print(a)

#indexing of strings
b = "csm"
print(b[0])
print(b[-1])

#reversing and slicing of the string
c = "nri institute of technology"
print(c[2:])
print(c[1:5])
print(c[::-1])

#looping of the string
for ch in c:
    print(ch)

#concatination of strings
c = "hi class"
d = "good morning"
print(c+d)    

#string repittion 
c = "csd"
print(c*5)

#members ship operator
x = "vijayawada"
print("j" in x)
print("z" not in x)






