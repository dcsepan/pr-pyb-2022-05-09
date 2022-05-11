# 1 Adott egy lista, és ennek elemeit kell kiírni vesszővel elválasztva. 
print("\n")
list = ["John Doe","Jack Doe", "Jane Doe"]
z = ""
for i in list:
    z += i + ", "
print(z)

# 2 Módosítsuk az előző feladatot, hogy ne legyen lezáró vesző 
print("\n")
list = ["John Doe","Jack Doe", "Jane Doe"]
z = ""
i = 0
for t in list:
    i += 1
    if i != 1:
        z += ", "
    z += t
print(z)

# 2 V2 forma Lista elemének megkapása, len()--Függvény
print("\n")
list = ["John Doe","Jack Doe", "Jane Doe"]
z = ""
i = 0
for t in list:
    i += 1
    z += t
    if i != len(list):
        z += ", "
print(z)

# 3 fizz buzz, Abban az esetben ha a szám osztható 3-mal akkor fizz-t kell mondani, ha 5-el osztható buzz
# ha mindkettővel osztható akkor Fizz Buzz
print("\n")
s = 0
for s in range(1, 101):
    if s % 15 == 0:
        print("FizzBuzz")
    elif s % 5 == 0:
        print("Buzz")
    elif s % 3 ==0:
        print ("Fizz")
    else:
        print(s) 


