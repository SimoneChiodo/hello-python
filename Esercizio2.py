# Crea una lista di numeri e stampa solo quelli pari.

# VERSIONE 1
# lista = [ 1, 2, 3, 4, 5, 6 ]
# for x in lista:
#   if (x % 2) == 0: 
#     print(x)

# VERSIONE 2
lista = [ 1, 2, 3, 4, 5, 6 ]
nuovaLista = []
for x in lista:
  if (x % 2) == 0: 
    nuovaLista.append(x)
print(nuovaLista, sep="-")
