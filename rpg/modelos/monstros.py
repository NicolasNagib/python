class Monstro:
    def __init__(self, nome, saude, dano ,arma, recompensa):
        self.nome = nome
        self.saude = saude
        self.dano = dano
        self.arma = arma
        self.recompensa = recompensa
    
    def __str__(self):
        return f"O {self.nome} possui {self.saude}HP"

    def receberDano(self, quantidade_dano):
        self.saude -= quantidade_dano
        if self.saude < 0:
            self.saude = 0

class Goblin(Monstro):
    def __init__(self, nome, saude, dano, arma, recompensa, tipo):
        super().__init__(nome, saude, dano, arma, recompensa)
        self.tipo = tipo
    
"""
1. criar goblin
2. o que ele precisa ter?


"""