import modelos.classesPersonagens as cp
import modelos.monstros as monstros
from time import sleep

class Ataque:
    def __init__(self, nome, dano, tipo, numero_alvos, tempo_recarga, efeito=""):
        self.nome = nome
        self.dano = dano
        self.tipo = tipo
        self.alvos = numero_alvos
        self.tempo_recarga = tempo_recarga
        self.efeito = efeito
        self.cooldown = 0
    
    def __str__(self):
        return f'{self.nome}'
    
    def usar(self, alvo):
        if self.cooldown == 0:
            self.cooldown = self.tempo_recarga
            alvo.receberDano(self.dano)
            print(f"O {alvo.nome} recebeu {self.dano} de dano! saude atual dele {alvo.saude}")

        else:
            sleep(1)
            print(f"Não foi possivel realizar o ataque espere o tempo de recarga: {self.cooldown}")

    def tick(self):
        if self.cooldown > 0:
            self.cooldown -= 1
    
def combate(jogador, inimigo):
    while inimigo.saude > 0:
        print(f"""
            [1] {jogador.ataques[0]}
            [2] Fugir
              """)
        acao = input("Escolha uma ação: ")
        if acao == "1":
            sleep(1)
            jogador.atacar(inimigo)
        elif acao == "2":
            print("Você fugiu com sucesso!!")
            break
        
        if inimigo.saude > 0:
            jogador.receberDano(inimigo.dano)
            sleep(1)
            print(f"Você recebeu 20 de dano! saude atual {jogador.saude}")
        else:

            print(f"{inimigo.nome} derrotado com sucesso!!")
            break
        jogador.ataque.tick()
        sleep(.5)