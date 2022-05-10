# Kérj be a felhasználótól egy egész számot! Majd amennyiben páros, írd ki, hogy páros, ha páratlan írd ki, hogy páratlan.
# Kérj be a felhasználótól egy másik egész számot, amennyiben nagyobb mint 0 írd ki hogy pozitív, ha 0-a írd ki hogy 0-a, ha negatív azt írd ki.
# Kérd be a felhasználó nevét! Ha nem írja be, írd ki, hogy "ez nem volt szép!"

# Feladat 1
print("1.Feladat")
print("\n")
name = input("Adjon egy szám?")
if int(name) % 2 == 0:
    print(f"Páros szám!")
else:
    print(f"Páratlan szám!")
print("\n")

#Feladat 2: 
print("2.Feladat")
print("\n")
name = input("Adjon egy szám?")
if int(name)  > 0:
    print(f"Pozitiv!")
else:
    print(f"Negatív!")
print("\n")

# 3 Feladat 
name = input("Add meg a neved!")
if (name == ""):
    print ("Ez nem volt szép!")

# Szorgalmi: egész szám -e, vagy lebegőpontos 
answer = input("adj meg egy számot!")
if int(float(answer)) == float(answer):
    print("Egész szám!")
else :
    print("Lebegőpontos")

