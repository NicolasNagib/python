from modelos.personagem import Personagem
from modelos.combate import Ataque

"""
Classes: 
    1. Mago
    2. Cavaleiro
    3. Bandido
"""

class Mago(Personagem):
    def __init__(self, nome, saude, defesa, mana, classe, ataque=None):
        super().__init__(nome, saude, defesa, mana, classe, ataque)
    def __str__(self):
        return f"{super().__str__()} e a magia inicial dele se chama {self.ataque}" 
    
class Cavaleiro(Personagem):
    def __init__(self, nome, saude, defesa, mana, classe, ataque=...):
        super().__init__(nome, saude, defesa, mana, classe, ataque)

    def __str__(self):
        return f"{super().__str__()} e o ataque inicial dele se chama {self.ataque}"
    
class Bandido(Personagem):
    def __init__(self, nome, saude, defesa, mana, classe, ataque=None):
        super().__init__(nome, saude, defesa, mana, classe, ataque)

    def __str__(self):
        return f"{super().__str__()} e a habilidade inicial dele se chama {self.ataque}"



