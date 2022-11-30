szoveg:str = input('szöveg: ')

for i in range(len(szoveg)):
    print(szoveg[len(szoveg) - i - 1], end='\0')
print(end='\n')

# ----------------------

karakterek:list[chr] = list[chr](szoveg)
karakterek.reverse()
szoveg = "".join(karakterek)
print(szoveg)