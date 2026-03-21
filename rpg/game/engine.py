from funcoes.fala import fala

from entities.classesPersonagens import Mago, Cavaleiro, Bandido
from game.world import (
    cripta_lua,
    descobrir_artefatos,
    descobrir_torre,
    ruinas_submersas,
    templo_chama_viva,
    templo_elgran,
    torres_das_cinzas,
)


def _escolher_classe(nome: str):
    fala("Escolha sua classe:")
    fala("[1] Mago")
    fala("[2] Cavaleiro")
    fala("[3] Bandido")
    escolha = input("Classe: ").strip()

    if escolha == "1":
        return Mago(nome)
    if escolha == "2":
        return Cavaleiro(nome)
    if escolha == "3":
        return Bandido(nome)

    fala("Classe inválida. Assumindo Mago por padrão.")
    return Mago(nome)


def start_game():
    print("=-" * 20)
    print("RPG de Terminal - Eltoria")
    print("=-" * 20)

    fala("Para iniciar sua jornada, insira seu nome: ")
    nome = input("Nome: ").strip()
    if not nome:
        nome = "Viajante"

    player = _escolher_classe(nome)
    # Combat usa `jogador.ataque` como ataque selecionado.
    if getattr(player, "ataques", None):
        player.ataque = player.ataques[0]

    # Estado do mundo/quest (usado pelo world.py)
    player.fragmentos = []
    player.mapa = False
    player.alarme_torre = False
    player.bencao_aguas = False

    fala("Iniciando jornada...")
    fala(
        "Você é um viajante que chegou recentemente nas terras do reino de Eltoria, um reino que já foi muito abençoado por luz e prosperidade, mas que hoje está cercada por trevas, após o lançamento de uma maldição por um necromante."
    )
    fala(
        "A jornada começa com rumores sobre artefatos e com uma torre escondida onde o mal se fortalece."
    )

    if not descobrir_torre(player):
        return
    if not descobrir_artefatos(player):
        return

    # Loop de exploração (menu simples)
    while True:
        opcoes = []

        # Fragmentos necessários (world.py define exatamente estes nomes)
        if "Fragmento da Chama Viva" not in player.fragmentos:
            opcoes.append(("Templo da Chama Viva", templo_chama_viva))
        if (
            "Fragmento da Chama Viva" in player.fragmentos
            and "Fragmento de Elgran" not in player.fragmentos
        ):
            opcoes.append(("Templo Congelado de Elgran", templo_elgran))
        if (
            "Fragmento de Elgran" in player.fragmentos
            and "Fragmento de Nymor" not in player.fragmentos
        ):
            opcoes.append(("Ruínas Submersas de Nymor", ruinas_submersas))
        if (
            "Fragmento de Nymor" in player.fragmentos
            and "Fragmento da Lua Quebrada" not in player.fragmentos
        ):
            opcoes.append(("Cripta da Lua Quebrada", cripta_lua))

        # Final
        if len(player.fragmentos) >= 4:
            opcoes.append(("Torre das Cinzas (final)", torres_das_cinzas))

        # Se não houver opção, encerramos.
        if not opcoes:
            fala("Nenhuma rota disponível agora. Encerrando.")
            return

        fala("\n=== Mapa de Eltoria ===")
        for idx, (nome_local, _) in enumerate(opcoes, start=1):
            fala(f"[{idx}] {nome_local}")
        fala("[0] Sair")

        escolha = input("Para onde você vai? ").strip()
        if escolha == "0":
            fala("Você abandona a jornada. Até a próxima.")
            return

        try:
            idx = int(escolha) - 1
            nome_local, func = opcoes[idx]
        except (ValueError, IndexError):
            fala("Escolha inválida. Tente novamente.")
            continue

        fala(f"Indo para: {nome_local}")
        ok = func(player)
        if not ok:
            fala("Sua jornada foi interrompida.")
            return

        if func is torres_das_cinzas:
            fala("Você libertou Eltoria das trevas. Fim do jogo.")
            return