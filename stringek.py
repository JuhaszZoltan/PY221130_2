string:str = 'ÁrVíZtŰrŐ TüKöRfÚrÓgÉp'

hossz:int = len(string)
print(f'karakterek száma: {hossz}')

for betu in string:
    print(betu, end=' ')

print(f'\nelső betűje: {string[0]}')

# string[0] = 'X'
print(string)

# függvények:
csupa_kisbetu:str = string.lower()
print(csupa_kisbetu)

csupa_nagybetu:str = string.upper()
print(csupa_nagybetu)

kapitalis:str = string.capitalize()
print(kapitalis)

title:str = string.title()
print(title)

kezdodik:bool = string.lower().startswith('árvíz')
if kezdodik: print('"árvíz"zel kezdődik')
else: print('NEM árvízzel kezdödik')

vegzodik:bool = string.upper().endswith('CICA')
if vegzodik: print('"CICA"val végződik')
else: print('nem "CICA"val végződik :(')

cserelt:str = string.lower().replace('árvíz', 'cica')
print(cserelt)

csunya:str = "   \t\t   a macskák szeretik a tejet;;;   \n\n"
szep:str = csunya.strip().strip(';')
print(szep)

kethexameter = '''
Miért legyek én tisztességes? Kiterítenek úgyis!
Miért ne legyek tisztességes! Kiterítenek úgyis.
'''

szavak:list[str] = kethexameter.split()
print(szavak)
print(f'szavak száma a szövegben: {len(szavak)}')

rekord:str = 'Kovács József;1983-09-17;Peugeto'
mezok:str = rekord.split(';')
print(mezok)