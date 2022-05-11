# Saját függvény készítése 
# Kiírni a nevemet meg életkorom

def print_employee(name ="Annonymus", year_of_birth=2000): #Függvény fej: def kulcsszó, név, formális paraméter lista, ()--> nincs paramétere paraméter, alatta behúzva értéke
    print(f"A {name} dolgozó {year_of_birth}-ben született.") # Függvény törzs itt az egész a függvény definíciója
    print(f"Fizetése 200000 Ft.") # Függvény törzs

# Konvenció szerint, függvény fájl elején van, két sortörés függvények között 
def add (a,b):
    result = a + b  # itt a result változó a függvény futásáig élnek, utána megszünnek 
    return result 


# Sok return lehet egy függvényben 
def is_even(number):
    if number % 2 ==0:
        return "PÁROS"
    else:
        return "PÁRATLAN"

def print_is_even(number):
    if number % 2 ==0:
        return "PÁROS"
    else:
        return "PÁRATLAN"
    
def adj_vissza_egy_szamot():
    return 12


# True-t ad vissza, hogyha a paraméter páros, ellenkező esetben False-t
def is_even_number ():
    return number % 2 == 0
    

print()
print_employee("John Doe", 1980) # hivása a függvénynek, itt a aktuális paraméterek
print_employee("Jack Doe", 1990)
t = "Jane Doe",
print_employee( t, 1995)
print_employee( "Jahne Smith")
print_employee()

print()
sum = add(8, 10)
print(sum)
print()
print(add(8,20))

print()
print(is_even(11))

print()
print_is_even(12)

print()
adj_vissza_egy_szamot()
print()
szam = adj_vissza_egy_szamot()
print(szam)


