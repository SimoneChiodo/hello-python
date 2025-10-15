# Simula un piccolo database in memoria con una lista di dizionari (es. elenco studenti).

database =  [ 
  {"nome": "Piero", "cognome": "Rossi", "corso": "Informatica"},
  {"nome": "Francesco", "cognome": "Verdi", "corso": "Meccanica"}
]

for i, studente in enumerate(database):
  print(f"Lo studente numero {i+1} è:")
  print(studente["nome"], studente["cognome"], studente["corso"], "\n", sep=", ")