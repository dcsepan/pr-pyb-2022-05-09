# 1. Kérj be számokat a felhasználótól addig, míg 0-át nem ad be. 
# 1. Írd ki a beadott számok összegét kilépéskor. 

n = 10
sum = 0
while n != 0:
    n = int(input("Adjon meg egy számot: "))
    sum += n
print(sum)


