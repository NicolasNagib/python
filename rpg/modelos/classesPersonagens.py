import modelos.listaAtaques as la
from modelos.personagem import Personagem
from modelos.combate import Ataque

"""
Classes: 
    1. Mago
    2. Cavaleiro
    3. Bandido
"""

class Mago(Personagem):
    def __init__(self, nome, saude=90, defesa=30, mana=16, ataque=None):
        super().__init__(nome, saude, defesa, mana)
        self.ataques=[
            Ataque(**la.mago_magias["furia_gelmir"]),
            Ataque(**la.mago_magias["tempestade_zamor"]),
            Ataque(**la.mago_magias["rancor_morte"]),
                    ]
        
    def __str__(self):
        return f"{super().__str__()} \n Classe: Mago \n Magia inicial: {self.ataque}" 
    
class Cavaleiro(Personagem):
    def __init__(self, nome, saude=110, defesa=110, mana=10, ataque=None):
        super().__init__(nome, saude, defesa, mana)
        self.ataques=[
            Ataque(**la.cavaleiro_ataques["golpe_giratorio"]),
            Ataque(**la.cavaleiro_ataques["ataque_pesado"]),
            Ataque(**la.cavaleiro_ataques["investida_escudo"]),
                    ]

    def __str__(self):
        return f"{super().__str__()}\n Classe: Cavaleiro \n Ataque inicial: {self.ataque}"


class Bandido(Personagem):
    def __init__(self, nome, saude=100, defesa=50, mana=9):
        super().__init__(nome, saude, defesa, mana)
        self.ataques = [
            Ataque(**la.bandido_ataques["ataque_furtivo"]),
            Ataque(**la.bandido_ataques["adaga_envenenada"]),
            Ataque(**la.bandido_ataques["golpe_rapido"])
        ]

    def __str__(self):
        return f"{super().__str__()} \n Classe: Bandido \n Habilidade: {self.ataque}"
    
    

