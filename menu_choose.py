# Feladat

menu = """
Mit akarsz csinálni?

1.Két számot összeadni
2.Két számot kivonni
"""
print(menu)
answer = input("Adja meg a feladat számát:")
if answer == "1":
    n1 = int(input("Első szám:"))
    n2 = int(input("Második szám:"))
    print(f"Összeg: {n1} + {n2} ={n1 + n2}")
elif answer == "2":
    n1 = int(input("Első szám:"))
    n2 = int(input("Második szám:"))
    print(f"Különbség: {n1} - {n2} ={n1 - n2}")
else:
    print("Nem ismeret művelet")








#q = input("Mit akarsz csinálni?:"\n"/1. Két számot összeadni."\n" 2. Két számot kivonni. ")
#a1 = "Adj meg egy számot"
#a2 = "Add meg a 2. számot"
#if in(q) == 1
#    sum = 0
 #   sum = a1 + a2
#elif in(q) == 2
 #   sum = a1 - a2
    
