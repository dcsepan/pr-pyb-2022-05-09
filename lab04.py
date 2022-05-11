# 1. Írjatok egy is_not_negativ logikai függvényt
# Ami True-t ad vissza, ha a szám nagyobb vagy egyenlő mint 0-a. 

# 2. Írjatok egy olyan get_circle_area() nevű függvényt,
# melynek átadva a kör sugarát, visszaadja annak területét , r négyzet*pi

# 3. Írjatok egy olyan get_rectangle_area() függvényt
# ami visszaadja, a két oldalhossz alapján annak a téglalapnak a területét!

# 4. Írjatok egy olyan absolute() nevű függvényt, ami visszaadja a szám abszolult értékét!

# 5. Írjatok egy olyan sum_numbers() függvényt, ami paraméterül kap számok listáját,
# visszaadja a számok összegét.

# 6. Írj egy  roll_dice()függvényt, ami visszaad egy 1-6 véletlen számot.

# 7 . Írj egy count_positiv_numbers() függvényt, ami paraméterül kap egész számok listáját
# és visszaadja, hogy hány pozitiv szám van benne. 

def is_not_negativ(number):
   return number >= 0

def get_circle_area(s):
    return (s * s) * 3.14

def get_rectangle_area(a,b):
    return (a * b)

def s_absolute(s):
    if  s >= 0:
        print(s)
    elif s < 0:
        print(s * (-1))
    
def sum_numbers(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

from random import randint
def roll_dice():
    s = randint (1 , 6)
    return s

def count_positiv_numbers(numbers):
    s = 0
    for i in numbers:
        if i > 0:
            s = s + 1
        return s

if __name__ == "__main__":   
        n1 = is_not_negativ(-30)
        print(n1)


        t = get_circle_area(10)
        print(f"Kör területe: {t}")

        t = get_rectangle_area(10,2)
        print(f"Téglalap területe: {t}")
        print ()

        absolute(-55)
        print ()

        numbers = [10,1,20,30,70,80]
        print(sum_numbers(numbers))
        print()

        print(roll_dice())
        
        numbers = [10,1,-20,-30,-70,80]
        print(count_positiv_numbers(numbers))
        print()

        # Tesztpiramis: milyen teszteket kell írni egy alkalmazáshoz:
            # End to End: Teszteli az egész klickelős API részt-
            # Integrációs tesztek: Több függvény együt működését teszteli 
            # Unit tesztek : Python esetén --> függvény
        # Tesztesetek: 
            # Előkészítés(Given)
            # Tesztelendő futatása(when)
            # Elvárt eredmény összehasonlítása (then) --> Assert 
            # Pythonban nem lehet tesztesetet írni csak a python használatával, van a pytest 

