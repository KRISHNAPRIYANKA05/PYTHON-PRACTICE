# dictionary methods 
#fromkeys():creates a new dictionary with specified keys and values 
e = {'one','two','three'}
e = dict.fromkeys(e,10)
print(e)

#setdefault():return the values of to specfied key if the key is in the dictionary 
# if not their insert the key with the specified value and return
k  ={1:'two','three':4,'four':5}
print(k.setdefault(1, 'default_value'))

#nested dictionary:a dictioanry with in dictioanr
L = {1:'three','four':5,'seven':{'r':1,'s':123}}
print(L['seven']['s'])

#dictioanary comprehension:a concise wayto create dictioanries
# a shoretest way to create a dictioanary 
d = {'a':1,'b':2,'c':3,'d':4}
d1 = {k:v*2 for k,v in d.items()}
print(d1)
