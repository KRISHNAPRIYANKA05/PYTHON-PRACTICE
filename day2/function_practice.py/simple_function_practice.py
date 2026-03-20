#in this we write programs on the functions write from the beggining

#even or odd by function
a = int(input("enter the value of a:"))
def even_or_odd(a):
    if a % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")
even_or_odd(a)