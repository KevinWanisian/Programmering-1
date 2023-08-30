# Läs in fem heltal från användaren
"""a = int(input("Ange tal a: "))
b = int(input("Ange tal b: "))
c = int(input("Ange tal c: "))
d = int(input("Ange tal d: "))
e = int(input("Ange tal e: "))

# Använd max-funktionen för att hitta det högsta värdet
Högsta = max(a, b, c, d, e)

# Presentera resultatet för användaren
print("Det högsta inmatade heltalet är" (Högsta))"""


tal_lista = []
for _ in range(5):
    tal = int(input(" Mata in ett heltal: "))
    tal_lista.append(tal)

hosta_tal = max(tal_lista)
print("Det högsta talet är: ", hosta_tal)


