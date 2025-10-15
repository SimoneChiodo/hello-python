# Leggi un file di testo e conta quante righe contiene. Sfrutta un try-catch in caso il file non esista.

# VERSIONE 1
# try:
#   file = open("text.txt", "r")
#   righe = file.readlines()
#   print(f"Il file contiene {len(righe)} righe!")
#   file.close()
# except FileNotFoundError:
#   print("File non trovato!")

# VERSIONE 2
try:
  with open("text.txt", "r") as file:
    righe = file.readlines()
    print(f"Il file contiene {len(righe)} righe!")
except FileNotFoundError:
  print("File non trovato!")