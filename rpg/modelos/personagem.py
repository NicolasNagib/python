from modelos.combate import Ataque


class Personagem:

    def __init__(self, nome, saude, defesa, mana, ataque=None):
        self.nome = nome
        self.saude = saude
        self.defesa = defesa
        self.mana = mana
        self.mapa = False
        self.alarme_torre = False
        self.fragmentos = []
        self.reliquia = ""
        self.ataque = ataque
        self.ataques = []
        self.ataques.append(self.ataque)
        self.xpNecessario = 100
        self.xpAcumulado = 0
        self.nivel = 1

        self.saudeMaxima = saude
        self.manaMaxima = mana
    
    def __str__(self):
        return f"O seu personagem se chama {self.nome}, ele possui: \nSaúde: {self.saude}HP \nDefesa: {self.defesa}DP \nMana: {self.mana}MP"
    
    def atacar(self, alvo):
        self.ataque.usar(alvo)
    
    def recuperarVida(self, quantidade_vida_recuperada):
        self.saude += quantidade_vida_recuperada

    def receberDano(self, quantidade_dano):
        self.saude -= quantidade_dano
    
    def recuperarMana(self, quantidade_mana_recuperada):
        self.mana += quantidade_mana_recuperada

    def receberXp(self,quantidade):
            self.xpAcumulado += quantidade
            print(f"Você recebeu {quantidade}Xp!!")
            while self.xpAcumulado >= self.xpNecessario:
                self.subirNivel()


    def subirNivel(self):
        if self.xpAcumulado >= self.xpNecessario:
            self.nivel +=1
            self.xpAcumulado= self.xpAcumulado - self.xpNecessario
            self.xpNecessario = 100*self.nivel**1.5
            print(f"Você evoluiu de nivel, parabéns agora está no nivel {self.nivel}")

            # Melhorando status
            self.saudeMaxima *= 1.5
            self.manaMaxima  *= 1.5
            self.saude = int(self.saudeMaxima)
            self.mana  = int(self.manaMaxima)

            # Mostrar status
            print(f"Saúde aumentada! -> {self.saude}Hp")
            print(f"Mana aumentada!  -> {self.mana}Mp")

    def ver_nivel(self):
        print(f"Seu nível é {self.nivel}, você possui {self.xpAcumulado}Xp e faltam {self.xpNecessario - self.xpAcumulado}Xp para o próximo nivel")
