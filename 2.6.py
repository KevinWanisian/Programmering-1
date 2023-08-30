vanligkorv = 20.95
veganskkorv = 34.95
dryck = 13.95

mat = int(input("Antal elever som äter 2 korvar"))
mat2 = int(input("Antal elever som äter 3 korvar"))
veganskmat = int(input("Antal elever som äter 2 veganska korvar"))
veganskmat2 = int(input("Antal elever som äter 3 veganska korvar"))
lask = int(input("Antal elever som vill ha läsk"))

matallt = ((mat * 2) + (mat2 * 3)) / 8
veganskallt = ((veganskmat * 2) + (veganskmat2 * 3)) / 4
Läsk = lask * dryck
kostnad = ((matallt * vanligkorv) + (veganskallt * veganskkorv) + Läsk)

print("Såhär många korvpaket ska köpas av vanlig korv:", round(matallt))
print("Såhär många korvpaket ska köpas av vegansk korv:", round(veganskallt))
print("Antal läsk:", lask)
print("Den totala kostnaden blir:", kostnad)

