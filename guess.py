from random import randint


n = randint(1,10)
s = False
while not s:
    g = int(input("Adj meg egy számot:"))
    if n < g:
        print("Kisebb")
    elif n > g: 
        print("Nagyobb")
    else:
        print("Eltaláltad")
        s = True