# Véletlenszám generátor

# V1
from random import randint, random, randrange, choice, shuffle



number = random() #Függvényes megoldás
print(number)

# V2 0-10 között generál egy véletlen számot, 10-et nem dobja bele --> baról zárt 
number = randrange(0, 10)
print (number)

# V3 0-6 mindkét oldalt zárt, kidobja a végén az értéket 3 vagy 6
number = randint(3, 6)
print (number)

# V4 
numbers = ["a" , "b" , "c" , "d"]
print (choice(numbers))

# V5
shuffle(numbers)
print(numbers)

print("\n")
# Feladat 
n = randint(0, 10)
s = False
while not s :
    i = int (input("Adj meg egy számot!: "))
    if n < i :
        print("Kisebb!")
    elif n > i:
        print("Nagyobb")
    else n == i:
        print("Kitaláltad!")