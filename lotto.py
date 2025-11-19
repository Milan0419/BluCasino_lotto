import random

lotto = []
for i in range(5):
    i = random.randint(1, 99)
    lotto.append(i)
    
print(lotto)

szamok = []
for i in range(5):
    while True:
        try:
            i = int(input("Írd be a lottószámod:"))
            szamok.append(i)
            break
        except ValueError:
            
        


for i in range(5):
    if lotto.count(szamok[i]) == 1:
        print("Helyes szám:")
        print(szamok[i])
        


print("A te számaid: ")
print(*szamok)
print('A helyes számok: ')
print(*lotto)