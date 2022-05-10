answer = input("Adj meg egy számot!")
if answer.isdecimal():
    print("Szám")
else:
    print("Nem szám")

print("\n") 

answer = input("Adj meg egy számot!")
try: 
    number = int(answer) #Ha itt hiba van, megy az except-re.
except:
    print("Nem szám")
print("End")