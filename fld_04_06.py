szoveg:str = input('szöveg: ')

c:int = 0
for b in szoveg:
    if b == 'e' or b == 'E': c += 1
print(f'az "E" betűk száma a szövegben: {c}')