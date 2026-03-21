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
            dano_aplicado = alvo.receberDano(self.dano)
            fala(
                f"O {alvo.nome} recebeu {dano_aplicado} de dano! "
                f"saude atual dele {alvo.saude}"
            )

        else:
            sleep(1)
            fala(f"Não foi possivel realizar o ataque espere o tempo de recarga: {self.cooldown}")

    def tick(self):
        if self.cooldown > 0:
            self.cooldown -= 1
    
def combate(jogador, inimigo) -> bool:
    """
    Retorna:
      True  -> inimigo derrotado
      False -> player fugiu / morreu
    """
    while inimigo.saude > 0 and jogador.saude > 0:
        ataque_txt = getattr(jogador.ataque, "nome", None) or "nenhum ataque selecionado"
        fala(
            f"""
            [1] {ataque_txt}
            [2] Fugir
            """
        )
        acao = input("Escolha uma ação: ")
        if acao == "1":
            sleep(1)
            jogador.atacar(inimigo)
        elif acao == "2":
            fala("Você fugiu com sucesso!!")
            return False
        else:
            fala("Ação inválida. Tente novamente.")
            sleep(0.5)
            continue
        
        if inimigo.saude > 0:
            dano_aplicado = jogador.receberDano(inimigo.dano)
            if jogador.saude <= 0:
                fala("Jogador derrotado!")
            else:
                fala(f"Você recebeu {dano_aplicado} de dano! saude atual {jogador.saude}")
        else:
            fala(f"{inimigo.nome} derrotado com sucesso!!")
            jogador.receberXp(inimigo.recompensa)
            return True

        if getattr(jogador, "ataque", None) is not None:
            jogador.ataque.tick()
        sleep(.5)

    return False