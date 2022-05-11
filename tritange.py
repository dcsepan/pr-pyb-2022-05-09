# Bónusz feladat: beadunk a classify_ractangle() függvénynek három számot, és a függvény visszaadja, hogy 
# szerkeszthető -e belőle háromnszög, és az derégszögű -e, egyenlő szárú, vagy szabályos 


def classify_tritangle(a,b,c):
        if a + b < c or a + c < b or b + c < a:
            return "Nem szerkeszthető háromszög."
        if a == b and b == c:
            return "Szabályos háromszög"
        triangle_class = ""
        if a ** a + b ** b == c ** c or a ** a + c ** c == b ** b or b * b + c * c == a * a:
            triangle_class = "Derékszögű"
        if a == b or a == c or c == b:
            triangle_class += "Egyenlőszárú"
        else: 
            triangle_class += "Általános"
        return triangle_class

# Ki lehet szervezni a műveleteket külön függvényben, és azt meghívni az első függvényben. 

print(classify_tritangle(1,2,4))
print()
print(classify_tritangle(2,2,2))
print()
print(classify_tritangle(3,4,5))
print()
print(classify_tritangle(2,2,4))
print()

# Dokumentációs megjegyzés: 
# függvény után írt strin, """ Blaba """
