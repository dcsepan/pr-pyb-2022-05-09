#Logika kifejezés: olyan kifejezés, melynek az eredménye bool típusu

has_two_eyes = True
print(has_two_eyes)
print(type(has_two_eyes))

#Egyenlőség vizsgálat == -jel
print(5 == 5)
# =-jel értékadás 

print(6 == 5)
number = 8
print(number == 8)
print(number)

print(number == 22)
print(number)

name = "John Doe"
print(name == "John Doe")
print(name == "Jack Doe")

print(5 > 10)
print( 5 < 10)
print(5 < 5)
print(5 <= 5)

#NOT Operátor
print (not True)
print (not False)
print(not 8 > 10) #Előbb 8>10 elvégzi, majd a not operátor jön 

#OR Operátor, ha egyik teljesül akkor True 
print(True or False) #True az eredmény
print(False or False) #False az eredmény
print(5 > 2 or 10 < 2) #True a kettő eredményét megnézi, és utána True+False= True 

#And, ha mindkettő teljesül akkor True 
print(True and True)
print(False and True)
print(False and False)
print("\n")
# Páros vagy páratlan eldöntése 
number = 7
print(number % 2 == 0)

