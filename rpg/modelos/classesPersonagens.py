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
        super().__init__(nome, saude, defesa, mana, ataque)
    def __str__(self):
        return f"{super().__str__()} \nClasse: Mago \nMagia inicial: {self.ataque}" 
    
    def escolherAtaque(self):
        print("""
              Escolha um feitiço inicial:
                [1] Fúria de Gelmir(Fogo, alvo único, tempo de recarga de 2 turnos, dano 20)
                [2] Tempestade de gelo de Zamor(Gelo , múltiplos alvos, tempo de recarga de 2 turnos, dano 10)
                [3] Rancor da morte antiga(Escuridão, alvo único, tempo de recarga de 2 turnos, dano 20)
              """)
        magia_inicial = input("Escolha uma magia inicial: ")
        if magia_inicial == "1":
            magia_inicial = {
                "nome" : "Fúria de Gelmir",
                "dano": 20,
                'tipo': "Fogo",
                "numero_alvos": "único",
                "tempo_recarga": 2,
                "efeito": "queimadura"
            }
        elif magia_inicial == "2":
            magia_inicial = {
                "nome" : "Tempestade de gelo de Zamor",
                "dano": 20,
                'tipo': "Gelo",
                "numero_alvos": "Múltiplos alvos",
                "tempo_recarga": 2,
                "efeito": "congelar"
            }
        elif magia_inicial == "3":
            magia_inicial = {
                "nome" : "Rancor da morte antiga",
                "dano": 20,
                'tipo': "Escuridão",
                "numero_alvos": "único",
                "tempo_recarga": 2,
                "efeito": ""
                }
            
        self.ataque = Ataque(magia_inicial['nome'], magia_inicial['dano'],magia_inicial['tipo'] ,magia_inicial['numero_alvos'], magia_inicial['tempo_recarga'], magia_inicial['efeito'])
        self.ataques.append(self.ataque)
        return f"Habilidade {magia_inicial} escolhida com sucesso!"

    
class Cavaleiro(Personagem):
    def __init__(self, nome, saude=110, defesa=110, mana=10, ataque=None):
        super().__init__(nome, saude, defesa, mana, ataque)

    def __str__(self):
        return f"{super().__str__()}\n Classe: Cavaleiro \nAtaque inicial: {self.ataque}"

    def escolherAtaque(self):
        print("""
              Escolha um ataque inicial:
                [1] Golpe giratório(Múltiplos alvos, tempo de recarga de 2 turnos ,dano 20)
                [2] Ataque pesado(Alvo único, tempo de recarga de 3 turnos, dano 40)
                [3] Investida com escudo(Alvo único, chance de atordoamento, tempo de recarga de 1 turno, dano 20)
              """)
        ataque_inicial = input("Escolha um ataque inicial: ")
        if ataque_inicial == "1":
            ataque_inicial = {
                "nome" : "Golpe giratório",
                "dano": 20,
                'tipo': "fisico",
                "numero_alvos": "múltiplos alvos",
                "tempo_recarga": 2,
                "efeito": ""
                }
        elif ataque_inicial == "2":
            
            ataque_inicial = {
                "nome" : "Ataque pesado",
                "dano": 40,
                'tipo': "fisico",
                "numero_alvos": "único",
                "tempo_recarga": 3,
                "efeito": ""
                }
        elif ataque_inicial == "3":
             
            ataque_inicial = {
                "nome" : "Investida com escudo",
                "dano": 20,
                'tipo': "fisico",
                "numero_alvos": "único",
                "tempo_recarga": 2,
                "efeito": "atordoamento"
                }

        self.ataque = Ataque(ataque_inicial['nome'], ataque_inicial['dano'],ataque_inicial['tipo'] ,ataque_inicial['numero_alvos'], ataque_inicial['tempo_recarga'], ataque_inicial['efeito'])
        self.ataques.append(self.ataque)
        return f"Habilidade {ataque_inicial} escolhida com sucesso!"

class Bandido(Personagem):
    def __init__(self, nome, saude=100, defesa=50, mana=9, ataque=None):
        super().__init__(nome, saude, defesa, mana, ataque)

    def __str__(self):
        return f"{super().__str__()} \nClasse: Bandido \nHabilidade inicial: {self.ataque[0]}"

    def escolherAtaque(self):
        print("""
              Ecolha uma habilidade inicial:
                [1] Ataque furtivo(Causa dobro de dano se for o primeiro ataque, tempo de recarga de 1 turno, dano 20)
                [2] Adaga envenenada(Dano por envenenamento 5 por turno, tempo de recarga 3 turnos, dano 15)
                [3] Golpe rápido(Ataque primeiro no turno, tempo de recarga 1 turno, dano 15)
              """)
        habilidade_inicial = input("Escolha uma habilidade inicial: ")

        if habilidade_inicial == "1":
            habilidade_inicial = {
                "nome" : "Ataque furtivo",
                "dano": 20,
                'tipo': "Físico",
                "numero_alvos": "único",
                "tempo_recarga": 1,
                "efeito": "dobra"
        }
        elif habilidade_inicial == "2":
            habilidade_inicial = {
                "nome" : "Adaga envenenada",
                "dano": 15,
                'tipo': "Veneno",
                "numero_alvos": "único",
                "tempo_recarga": 3,
                "efeito": "envenenar"
            }
        elif habilidade_inicial == "3":
            habilidade_inicial = {
                "nome" : "Golpe rápido",
                "dano": 15,
                'tipo': "Físico",
                "numero_alvos": "único",
                "tempo_recarga": 1,
                "efeito": "prioridade"
                }
        self.ataque = Ataque(habilidade_inicial['nome'], habilidade_inicial['dano'],habilidade_inicial['tipo'] ,habilidade_inicial['numero_alvos'], habilidade_inicial['tempo_recarga'], habilidade_inicial['efeito'])
        self.ataques.append(self.ataque)
        return f"Habilidade {habilidade_inicial} escolhida com sucesso!"
