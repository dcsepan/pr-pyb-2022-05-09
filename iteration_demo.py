# Dry - don't repeat yourself. 

#n = int(input("Hányszor írja kia a neved."))
#for i in range (n):
#    print("David") #(indent=behúzás)előtte lehet tab vagy space, de csak az egyiket lehet használni

for i in range (10):
    print(i, "David")

for c in "hellopython".upper():
    print(c)

for i in range (2 * 4):
    print(i)

for e in [3, 9, 11, 2, 8]:
    print(e)
#Range fürggvény paraméter: 

for i in range(10): #Egyparaméteres
    print(i)
print("\n")
for i in range (5,10): # két paraméteres
    print(i)
print("\n")
for i in range(10, 100, 5): #Step by step megy 5-sével 10-től 100-ig
    print(i)
print("\n")
