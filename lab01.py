# Írd ki egymás után 5x a neved. 
# Írd ki egymás után 5x a neved, de írj elé sorszámot is. 0-tól
# Írd ki egymás után 5x a neved, de írj elé sorszámot is. 1-tól
# Írd ki az első 10 pozitív egész számot és mellé annak négyzetét! 1 - 1 2-4 , 10 is legyen benne. 
# Hónapok! írd ki az első 6 hónapra: Az év 1. hónapja január. months= ["január" , "február"]

# Feladat 1
print("1. Feladat kezdete!")
print("\n")
for i in range (5):
    print("Dávid")
print("1. Feladat vége!")
print("\n")


# Feladat 2 
print("2. Feladat kezdet!")
print("\n")
i = 0 
while i < 5 : 
    print(i,".", "Dávid",sep="")  
    i = i + 1  
print("2. Feladat vége!")
print("\n")


# Feladat 3 
print("3. Feladat kezdet!")
print("\n")
i = 1 
while i < 6 : 
    print(i,".", "Dávid",sep="")  
    i = i + 1  
print("3. Feladat vége!")
print("\n")


# Feladat 4 
print("4. Feladat kezdet!")
print("\n")
i = 1
while i <=10:
     print(f"{i} - {i*i}")
     i = i + 1
print("4. Feladat vége!")
print("\n")


# Feladat 5 
print("5. Feladat kezdet!")
print("\n")
i = 1
months = ["január", "február" , "március" , "április" , "május" , "június"]
for month in months:
    print(f"Az év {i}. hónapja {month}.")
    i = i + 1 
print("5. Feladat vége!")
print("\n")

