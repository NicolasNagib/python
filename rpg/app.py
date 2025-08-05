import modelos.classesPersonagens as cp
import modelos.monstros as monstros
import modelos.combate as combate
import modelos.roteiro as roteiro
from time import sleep
"""
1. Criação de personagem
2. Sistema de vida e ataque
3. Criação de Classes de personagens(mago, bardo, etc)
4. Sistema de itens
5. RPG
"""



def main():
    print("-="*10)
    print("D&D")
    print("-="*10)

    nome = input("Qual seria o seu nome, nobre guerreiro? ")
    print("""
            Escolha uma dessas classes e não se arrependerá:
                [1] Cavaleiro(Forte, porém lento)
                [2] Mago(Sábio, porém pouco resistente)
                [3] Bandido(Rápido, porém frágil)
          """)
    classe = input("Insira um valor para prosseguir: ")

    if classe == "1":
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

        jogador = cp.Cavaleiro(nome, 110, 110, 10, classe, ataque_inicial)

    elif classe == "2":
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

        jogador = cp.Mago(nome, 90, 30, 16, classe, magia_inicial)
    
    elif classe == "3":
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


        jogador = cp.Bandido(nome, 100, 50, 9, classe, habilidade_inicial)
    print(jogador)
    print("Iniciando jornada...")
    print("Você é um viajante que chegou chegou recentemente nas terras do reino de Eltoria, um reino que já foi muito abençoado por luz e prosperidade, mas que hoje está cercada por trevas, após o lançamento de uma maldição por um necromante")
    print("Sua jornada se inicia na floresta nebulosa, local de forte presença mágica e criaturas selvagens")
    goblin = monstros.Goblin("Goblin", 40, 20,"Adaga quebrada", "15XP" ,"Vermelho")
    print(f"Ao explorar um pouco a floresta você se depara com um {goblin.nome} {goblin.tipo}!")
    print("Iniciando combate")

    combate.combate(jogador, goblin)

    print(f"Após derrotar o goblin, o guerreiro encontra vestígios de um acampamento abandonado — com documentos queimados falando sobre um \"Selo Negro\" e uma torre oculta além das colinas.")
    print("Mais adiante o guerreiro chega a uma vila, e então fala com os moradores locais em busca de alguma pista")
    print("Os moradores comentam sobre a maldição, lançada pelo necromante Malakar")
    print("Eles comentam também que um artefato que outrora trouxe luz foi roubado e dividido em 4 fragmentos espalhados pelas terras do reino.")
    print("Este artefato, pode enfraquecer a maldição de Malakar e assim derrotá-lo")
    print("""Diante disso você se depara com tres escolhas:
          [1] Descobrir mais sobre os artefatos
          [2] Decobrir sobre a maldição
          [3] Sair em busca da torre oculta
          """)
    acao = input("Escolha um caminho:")
    if acao == "1":
        roteiro.descobrir_artefatos(jogador)
    elif acao == "2":
        roteiro.descobrir_torre(jogador)
    elif acao == "3":
        print("Movido pela coragem (ou talvez pela pressa), o guerreiro parte em direção às colinas amaldiçoadas em busca da torre oculta.")
        print("Após dias de viagem, ele encontra um campo devastado, onde a vegetação morreu e o ar é pesado.")
        print("Ali, cercada por uma neblina densa e sussurros fantasmagóricos, está a entrada da Torre das Cinzas.")
        print("Ao tentar se aproximar, o guerreiro sente sua energia vital enfraquecer...")
        print("Uma força invisível o impede de entrar. Vozes ecoam: 'Aquele que não carrega a luz será devorado pelas trevas...'")
        print("O guerreiro compreende então que precisa do artefato para enfrentar o mal supremo que habita a torre.")
        print("Ele decide então retornar à vila e seguir em busca dos fragmentos perdidos.")
        roteiro.descobrir_artefatos(jogador)
        acao = input("Antes de deixar a vila, deseja saber mais sobre a maldição?[s/n]")
        if acao == "s":
            roteiro.descobrir_torre(jogador)
    

    print("\nAgora com as informações em mãos e o mapa dos quatro templos, você pode escolher para onde irá em busca do primeiro fragmento do artefato:")
    print("""
        [1] Templo da Chama Viva (Nível recomendado: 10)
        [2] Templo Congelado de Elgran (Nível recomendado: 20)
        [3] Ruínas Submersas de Nymor (Nível recomendado: 25) [Requer benção das águas]
        [4] Cripta da Lua Quebrada (Nível recomendado: 30)
    """)

    destino = input("Escolha seu destino: ")

    if destino == "1":
        print("Você segue em direção ao Templo da Chama Viva, cruzando desertos secos e campos devastados pela fé cega do culto que lá reside...")
        roteiro.templo_chama_viva(jogador)
    elif destino == "2":
        print("Você parte para o norte, rumo às terras congeladas de Elgran, onde o frio congela até a esperança...")
        roteiro.templo_elgran(jogador)

    elif destino == "3":
        print("Você tenta seguir para as ruínas submersas de Nymor, mas se lembra que precisa da Benção das Águas para sobreviver ao oceano profundo...")
        print("Será necessário procurar um sacerdote das marés ou completar uma missão secundária para obter essa benção.")
        roteiro.ruinas_submersas(jogador)

    elif destino == "4":
        print("Você se prepara para a jornada mais perigosa de todas: a Cripta da Lua Quebrada. Um lugar onde a luz foi traída e as almas ainda choram em agonia...")
        roteiro.cripta_lua(jogador)

    fragmentos_necessarios = [
    "Fragmento da Chama Viva",
    "Fragmento de Elgran",
    "Fragmento de Nymor",
    "Fragmento da Lua Quebrada"
    ]

    if all(frag in jogador.fragmentos for frag in fragmentos_necessarios):
        print("Você reuniu todos os fragmentos!")
        print("O Coração da Luz se forma diante dos seus olhos, irradiando energia sagrada.")
        jogador.reliquia = "Coração da Luz"
    else:
        print("Você ainda não possui todos os fragmentos necessários...")
        faltando = [f for f in fragmentos_necessarios if f not in jogador.fragmentos]
    print("Fragmentos restantes:", ", ".join(faltando))

    if jogador.reliquia == "Coração da Luz":
        roteiro.torre_das_cinzas(jogador)

if __name__ == "__main__":
    main()

    