# Kérjünk be a felhasználótól számokat, írjuk ki addig a képernyőre amíg nem 0-a.
# Fejlesszük tovább úgy, ha 0-át ad meg, akkor ne írja ki a számot, hanem írja ki: "exit"

# Version 1
#number = 10
#while not number == 0:
#    number = int( input("Adj meg egy számot?: "))
#    if number == 0:
 #       print(f"exit")
 #   else:
#        print(f" A szám: {number}")
print("\n")
print("\n")
# Version 2
should_input_number = True
while should_input_number:
    number= int(input("Adj meg egy számot!: "))
    if number != 0:
        print(f"Szám: {number}")
    else:
        should_input_number = False
print("End")
