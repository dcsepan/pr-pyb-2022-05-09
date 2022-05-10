for i in range(5): # Feltételeket és ciklusokat egymásba lehet ágyazni
    for c in "alma":
        print(str(i) + c)

# Írjátok ki a szorzótáblát, két egymásba ágyazot ciklussal
    #Egy ciklus ami a sorokon megy végig
    #Az előző ciklus magjába kell egy ciklus 1-10-ig szintén 
#line = ""
#for i in range (1, 11):
#   line += str(i)
#print(line)
#print("\n")

print("\n")
content = ""
for i in range (1,11):
    for j in range (1,11):
        result = i * j
        content += str(result)
        if result < 10:
            content += " "
            content += str(result)
        elif result < 100:
            content += "  "
            content += str(result)
        content += "\n"
print(content)

print("\n")
# Hozz létre egy listát, mely egész számokat tartalmaz.
print("\n")
numbers = [43, 32, 43,532,31,16,17]
sum = 0
for number in numbers:
    sum += number
print(sum)

# Hozz létre egy listát mely + és - számokat tartalmaz, add össze a + -számokat
print("\n")
numbers = [42,-2,15,-8,10,9,432,-500]
sum = 0
for number in numbers:
    if (number > 0) : 
        sum += number
print(sum)

# Hozz létre egy listát mely + és - számokat tartalmaz, add össze a számok abszolult értékét.
numbers = [42,-2,15,-8,10,9,432,-500]
sum = 0
x= -1
for number in numbers:
    if (number < 0) : 
        sum += (number * x)
    else:
        sum += number
print(sum)






    

