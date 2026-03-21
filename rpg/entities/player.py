from __future__ import annotations


class Personagem:
    def __init__(self, nome: str, saude: int, defesa: int, mana: int):
        self.nome = nome

        # Atributos principais do combate
        self.saude = saude
        self.defesa = defesa
        self.mana = mana

        # Progressão
        self.ouro = 0
        self.xp = 0
        self.nivel = 1

        # Ataques
        self.ataques = []
        # Ataque "selecionado" que o combate usa (o jogador pode mudar depois)
        self.ataque = None

    def __str__(self) -> str:
        ataque_nome = getattr(self.ataque, "nome", None)
        ataque_txt = ataque_nome if ataque_nome else "nenhum"
        return (
            f"{self.nome} (Lv {self.nivel})\n"
            f"HP: {self.saude} | Defesa: {self.defesa} | Mana: {self.mana}\n"
            f"Ataque selecionado: {ataque_txt}"
        )

    def atacar(self, inimigo) -> None:
        if self.ataque is None:
            if not self.ataques:
                return
            self.ataque = self.ataques[0]
        self.ataque.usar(inimigo)

    def receberDano(self, quantidade_dano: int) -> int:
        """
        Retorna o dano realmente aplicado (descontando defesa).
        """
        dano_final = max(0, int(quantidade_dano) - int(self.defesa))
        self.saude -= dano_final
        if self.saude < 0:
            self.saude = 0
        return dano_final

    def receberXp(self, quantidade_xp: int) -> None:
        quantidade_xp = int(quantidade_xp)
        self.xp += quantidade_xp

        # Crescimento simples por níveis.
        # (mantém o jogo jogável sem precisar de sistema completo de loot/tiers)
        while self.xp >= self.nivel * 100:
            self.nivel += 1
            self.saude += 20
            self.defesa += 5
            self.mana += 5


class Player(Personagem):
    """
    Compatibilidade com o código antigo: caso alguém crie `Player(nome)`,
    ele vira um personagem genérico.
    """

    def __init__(self, nome: str):
        super().__init__(nome=nome, saude=100, defesa=5, mana=10)