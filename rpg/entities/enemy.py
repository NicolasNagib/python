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
        quantidade_dano = int(quantidade_dano)
        dano_aplicado = min(self.saude, quantidade_dano)
        self.saude -= dano_aplicado
        return dano_aplicado

class Goblin(Monstro):
    def __init__(self, nome, saude, dano, arma, recompensa, tipo):
        super().__init__(nome, saude, dano, arma, recompensa)
        self.tipo = tipo
    
"""
1. criar goblin
2. o que ele precisa ter?


"""