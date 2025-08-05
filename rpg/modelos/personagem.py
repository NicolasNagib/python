from modelos.combate import Ataque


class Personagem:

    def __init__(self, nome, saude, defesa, mana, classe, ataque=None):
        self.nome = nome
        self.saude = saude
        self.defesa = defesa
        self.mana = mana
        self.classe = classe
        self.mapa = False
        self.alarme_torre = False
        self.fragmentos = []
        self.reliquia = ""
        self.ataque = Ataque(ataque['nome'], ataque['dano'],ataque['tipo'] ,ataque['numero_alvos'], ataque['tempo_recarga'], ataque['efeito'])
        self.ataques = []
        print(self.ataque)
        self.ataques.append(self.ataque)
        self.xp = self.ver_nivel()
    
    def __str__(self):
        return f"O seu personagem se chama {self.nome}, ele possui {self.saude}HP {self.defesa}DP {self.mana}MP e a classe dele é {self.classe}"
    
    def atacar(self, alvo):
        self.ataque.usar(alvo)
    
    def recuperarVida(self, quantidade_vida_recuperada):
        self.saude += quantidade_vida_recuperada

    def receberDano(self, quantidade_dano):
        self.saude -= quantidade_dano
    
    def recuperarMana(self, quantidade_mana_recuperada):
        self.mana += quantidade_mana_recuperada

    def ver_nivel(self):
        if self.xp >= 10:i