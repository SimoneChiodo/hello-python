# Scrivi uno script che chieda nome e età all’utente e stampi quanti anni avrà tra 10 anni.

# VERSIONE 1
# nome = input("Come ti chiami? ")
# eta = input("Quanti anni hai? ")
# eta = int(eta) + 10
# print("Ciao " + nome + "! Tra 10 anni avrai " + str(eta) + " anni!")


nome = input("Come ti chiami? ")
eta = int(input("Quanti anni hai? "))
print(f"Ciao {nome}! Tra 10 anni avrai {eta + 10} anni!\n")