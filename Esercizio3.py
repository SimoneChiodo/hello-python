# Definisci una classe Persona con attributi nome e eta e un metodo saluta().

# VERSIONE 1
# class Persona:
#   def __init__(self, nome, eta):
#     self.nome = nome
#     self.eta = eta

#   def saluta(self):
#     print(f"Ciao, sono {self.nome} e ho {self.eta} anni!")

# persona = Persona("Pietro", 31)
# persona.saluta()

# VERSIONE 2
class Persona:
  def __init__(self, nome, eta):
    self.nome = nome
    self.eta = eta

  def __str__(self):
    return f"Ciao, sono {self.nome} e ho {self.eta} anni!"

persona = Persona("Piero", 32)
print(persona)