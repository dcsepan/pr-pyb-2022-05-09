# Függvények
# Amit megadunk a függvénynek, az a paramétere
# Amit visszaad a függvény, az a visszatérési értéke
# Ha mást is csinál a függvény, az a mellékhatás 
# Van neve, ill. paraméterlistája ,-vel elválasztva

print() # O-a paraméter
print("alma") # 1 paraméter
print("alma", "körte") # 2 paraméter
print("alma", "körte", sep ="") # sepp = "" mi legyen az elválasztó karakter
print("alma", "körte", end ="+-") # end = "" mi legyen a sortörő karakter 
# print: mellékhatása kiír vmit. a konsolera
# print: nincs visszatérési értéke 
# print: built in function 
print("\n")
# Függvény: 1 paramétere van, van visszatérési értéke--> paraméter típusa
type_of_number = type(15)
print(type_of_number)
print("\n")

print(type(15))

number = int("15")
print(number)

print(int("15"))

number = 10 + int("15")
print(number)

# beépített:  str() , float(), input(), print(), len(), range()
# külön modulos: random(), randrange(), randint() , choise()
print()
print()

