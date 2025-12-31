from platform import python_compiler
import modelos.classesPersonagens as cp
import modelos.monstros as monstros
from funcoes.fala import fala
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
            fala(f"O {alvo.nome} recebeu {self.dano} de dano! saude atual dele {alvo.saude}")

        else:
            sleep(1)
            fala(f"Não foi possivel realizar o ataque espere o tempo de recarga: {self.cooldown}")

    def tick(self):
        if self.cooldown > 0:
            self.cooldown -= 1
    
def combate(jogador, inimigo):
    while inimigo.saude > 0:
        fala(f"""
            [1] {jogador.ataque}
            [2] Fugir
              """)
        acao = input("Escolha uma ação: ")
        if acao == "1":
            sleep(1)
            jogador.atacar(inimigo)
        elif acao == "2":
            fala("Você fugiu com sucesso!!")
            break
        
        if inimigo.saude > 0:
            jogador.receberDano(inimigo.dano)
            if jogador.saude <= 0:
                fala("Jogador derrotado!")
                fala("Deseja iniciar um novo jogo?")
                escolha = input("Escolha(Sim/Não): ").capitalize()
                if escolha == "Sim":
                    break
            else:
                fala(f"Você recebeu 20 de dano! saude atual {jogador.saude}")
        else:

            fala(f"{inimigo.nome} derrotado com sucesso!!")
            jogador.receberXp(inimigo.recompensa)

            break
        jogador.ataque.tick()
        sleep(.5)