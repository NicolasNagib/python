def descobrir_artefatos(jogador):
    print("Após decidir isso você sai em busca do arqueólogo da cidade, ele conta que os artefatos estão protegidos em quatro templos: ")
    print("Templo da chama viva: um local que já serviu como centro de guia espiritual, mas que hoje é ocupado por um culto, que realiza sacrifícios humanos, esperando que as trevas se dissipem, e assim a luz retorne")
    print("Nivel recomendado: 10")
    print("Templo congelado de Elgran: este lugar é protegido pelo espírito de Elgran, um dragão de gelo maligno, que congelou as terras ao redor do templo, onde hoje elas abrigam golens de gelo, e o terrível Yeti")
    print("Nivel recomendado: 20")
    print("Ruínas submersas do templo de Nymor: Lugar onde outrora abrigava incriveis criaturas marinhas, hoje é o esconderijo do Kraken, a criatura mais poderosa dos oceanos")
    print("Nivel recomendado: 25, Relíquia necessária: Benção das águas")
    print("Cripta da Lua quebrada: Lugar onde Malakar evoluiu seus poderes, antigamente este lugar era um santuário dedicado a deusa Lunala")
    print("Nivel recomendado: 30")
    print("Após descobrir mais sobre o lugar, o guerreiro ganha um mapa onde ele pode escolher para onde ir")
    jogador.mapa = True

def descobrir_torre(jogador):
    print("O guerreiro se encontra com o ancião da vila, o ancião conta que Malakar está absorvendo as almas das pessoas para se fortalecer, também conta que a torre oculta é o esconderijo de Malakar, mas explica que não recomenda ir lá sem o artefato, pois sem ele o guerreiro será consumido pelas trevas")
    jogador.alarme_torre = True

def templo_chama_viva(jogador):
    print("Você se aproxima do Templo da Chama Viva, um antigo santuário agora consumido por trevas e fanatismo.")
    print("Chamas altas dançam nas torres do templo. O calor é sufocante. O ar cheira a enxofre e madeira queimada.")
    print("Ao chegar à entrada, você é observado por olhos ocultos entre as colunas de pedra negra.")
    print("De repente, três sacerdotes maníacos surgem — suas túnicas estão em chamas, mas eles parecem não sentir dor.")
    print("Sacerdote: 'Mais um tolo em busca da luz perdida... Você será o próximo sacrifício!'")

    print("\nVocê se prepara para o combate!")

    # (aqui você pode chamar: combate.combate(jogador, sacerdote1), etc.)

    print("\nApós derrotar os fanáticos, você entra no templo em ruínas.")
    print("O chão está repleto de símbolos gravados em sangue e brasas acesas por todo o salão.")
    print("No centro do templo, um altar flamejante queima com fogo eterno — e sobre ele, uma figura sombria observa em silêncio.")

    print("É o Guardião da Chama — outrora protetor da luz, agora corrompido pela promessa do poder eterno.")
    print("Guardião: 'Eu protejo o fragmento da luz... Mas não para você. Prove-se digno ou queime!'")

    print("\nVocê se prepara para enfrentar o Guardião da Chama.")

    # (aqui: combate final - ex: combate.combate(jogador, guardiao_chama))

    print("\nCom muito esforço, você derrota o Guardião.")
    print("As chamas ao redor do altar diminuem e revelam o 1º Fragmento da Luz.")
    print("Você sente uma energia pura e poderosa preencher seu corpo.")
    print("Você obteve: Fragmento da Luz (1/4)")
    jogador.fragmentos.append("Fragmento da Chama Viva")

    print("Ao deixar o templo, você escuta uma voz ecoando nas paredes:")
    print("'Os outros fragmentos esperam... Mas a escuridão também.'")

    print("Sua jornada continua...")

def templo_elgran(jogador):
    print("Você parte rumo ao norte, onde os ventos são cortantes e a neve nunca derrete.")
    print("Após dias de viagem por vales gelados e rios congelados, você avista a entrada do Templo Congelado de Elgran.")
    print("Esculturas de dragões adornam o portão, cobertas por gelo grosso. O silêncio é absoluto, como se o próprio tempo estivesse congelado ali.")
    print("Ao entrar, o frio é tão intenso que congela sua respiração. Você sente sua energia sendo drenada lentamente.")
    print("De repente, criaturas começam a emergir do chão de gelo... são Golens de Gelo, guardiões antigos do templo!")

    print("\nVocê entra em combate contra os Golens de Gelo!")

    # Exemplo: combate.combate(jogador, golem1)

    print("\nAo derrotá-los, você avança por um salão onde espelhos de cristal refletem sua imagem de maneira distorcida.")
    print("No fim do corredor, um santuário antigo guarda uma fonte congelada — e nela, um espírito feminino de aparência etérea.")

    print("Espírito: 'Você é corajoso. Antes que enfrente Elgran, receba minha bênção.'")
    print("Ela toca sua testa e você sente uma energia aquática percorrer seu corpo.")

    print("Você recebeu: **Benção das Águas**")
    print("Com ela, você poderá respirar e se mover livremente nas profundezas das Ruínas de Nymor.")

    print("Você encontra inscrições nas paredes — histórias perdidas de Elgran, o Dragão de Gelo que selava os espíritos das tempestades.")
    print("Mais adiante, uma ponte de gelo suspensa leva até um altar de gelo azul brilhante.")
    print("Mas antes de chegar ao fim, um rugido profundo ecoa pelas paredes do templo...")

    print("Elgran desperta de seu sono milenar!")

    print("Elgran: 'Você ousa pisar neste santuário sagrado? O frio eterno será sua prisão!'")
    print("O dragão de gelo colossal se ergue entre estalactites congeladas, com olhos brilhando como safiras.")
    print("Você não tem escolha: precisa enfrentá-lo para recuperar o segundo fragmento!")

    print("\nCombate épico contra Elgran, o Dragão de Gelo!")

    # Exemplo: combate.combate(jogador, elgran)

    print("\nApós um confronto árduo, você derrota Elgran.")
    print("Seu corpo congela em cristais de gelo puro e se desfaz em pó brilhante.")
    print("No centro do altar, protegido por runas antigas, repousa o segundo Fragmento da Luz.")
    print("Você sente uma onda gélida de poder fluir até seu coração.")

    print("Você obteve: Fragmento da Luz (2/4)")
    jogador.fragmentos.append("Fragmento de Elgran")
    print("O templo começa a ruir, como se seu propósito tivesse sido cumprido.")

    print("Você corre para fora antes que tudo desmorone.")
    print("Do alto da montanha congelada, observa ao longe... ainda restam dois fragmentos, e a jornada está longe do fim.")

def ruinas_submersas(jogador):
    print("Você parte em direção ao sul, onde o mar encontra os pântanos e os ventos carregam o cheiro de sal e podridão.")
    print("As águas estão escuras, e a maré parece recuar ao sentir sua aproximação.")
    print("Graças à Benção das Águas, você respira fundo e mergulha...")

    print("Você adentra um abismo submerso, onde a luz desaparece rapidamente.")
    print("No fundo do oceano, encontra estruturas antigas cobertas por corais e algas. As Ruínas de Nymor, esquecidas por séculos.")

    print("Enquanto explora os corredores submersos, sombras se movem ao seu redor...")
    print("Sirenas corrompidas sussurram melodias mortais, tentando te atrair para armadilhas.")
    print("Você se vê obrigado a lutar.")

    # Exemplo:
    # combate.combate(jogador, sirena1)

    print("Após escapar do encanto das sirenas, você chega a uma praça circular submersa.")
    print("Uma grande escadaria de pedra leva a uma cripta selada com símbolos antigos do mar.")

    print("Você encosta a mão e os símbolos brilham com a energia da Benção das Águas.")
    print("A passagem se abre... e uma corrente forte te suga para o fundo.")

    print("Você acorda em uma câmara escura, com colunas destruídas e conchas gigantes presas nas paredes.")
    print("O chão começa a tremer... e então, os tentáculos do **Kraken** surgem da escuridão.")

    print("Kraken: 'Você ousa perturbar o sono do abismo? Que os mares silenciem sua alma.'")

    print("Inicia-se o combate contra o Kraken — o maior guardião do templo.")

    # combate.combate(jogador, kraken)

    print("A batalha é brutal. O Kraken ataca com tentáculos gigantes, jatos d'água e tenta te puxar para as profundezas.")
    print("Mas após muita resistência, ele solta um último rugido aquático e se desfaz em espuma abissal.")

    print("No centro da arena, um altar se ergue com o **Terceiro Fragmento da Luz**, flutuando em uma bolha de água pura.")

    print("Você obteve: Fragmento da Luz (3/4) ")
    jogador.fragmentos.append("Fragmento de Nymor")
    print("A água ao redor se purifica, e as ruínas parecem respirar pela primeira vez em séculos.")
    print("Você retorna à superfície, sentindo-se mais forte... mas também mais próximo do fim.")

def cripta_lua(jogador):
    print("Você segue rumo às montanhas esquecidas, onde o céu parece mais pesado e a lua raramente brilha.")
    print("Após atravessar cavernas de pedras negras e florestas mortas, você encontra uma entrada semi-soterrada por ossos e símbolos distorcidos.")
    print("A Cripta da Lua Quebrada... outrora um santuário de luz, agora apodrecido pelo toque das trevas.")

    print("Ao adentrar, você sente um frio que não vem do vento, mas da própria alma do lugar.")
    print("Nas paredes, inscrições lunares foram riscadas, manchadas com sangue e transformadas em runas de necromancia.")

    print("Vultos sussurram nos corredores. Espíritos corrompidos da antiga ordem da deusa Lunala surgem.")
    print("Eles foram convertidos em guardiões mortos-vivos por Malakar.")

    print("Você precisa enfrentá-los para continuar.")

    # combate.combate(jogador, espectro1)

    print("Com as almas libertadas, um dos espectros aponta para uma porta selada com símbolos lunares partidos.")
    print("Você precisa resolver um enigma para abri-la...")

    print("Enigma: 'Sou a luz que não brilha, a sombra que ilumina. Quando caio, tudo dorme. Quem sou eu?'")
    resposta = input("Sua resposta: ").strip().lower()

    if resposta in ["lua", "a lua"]:
        print("Os símbolos brilham brevemente com luz prateada. A porta se abre.")
    else:
        print("Nada acontece. Uma força te empurra para trás. Você tenta novamente até acertar.")
        # Poderia repetir ou forçar combate adicional

    print("Atravessando a porta, você encontra um salão circular com vitrais quebrados e um altar negro.")
    print("No centro, uma figura encapuzada, de costas para você, murmura palavras sombrias.")

    print("??? : 'A Deusa da Lua os abandonou... mas eu? Eu os ouvi. Eu dei poder a eles.'")
    print("O ser se vira — é um antigo sacerdote, agora completamente deformado pela magia negra.")

    print("Sacerdote Caído: 'Não deixarei que leve a última centelha de luz.'")

    print("Inicia-se o combate contra o **Sacerdote da Lua Corrompido**!")

    # combate.combate(jogador, sacerdote)

    print("O sacerdote ataca com feitiços lunares corrompidos, invoca almas e manipula a escuridão para confundir você.")
    print("Mas ao ser derrotado, ele olha para o céu, e por um segundo... a lua ressurge através de uma fresta no teto.")

    print("Uma última luz ilumina o altar. Você caminha até ele e encontra o **último Fragmento da Luz**.")

    print("Você obteve: Fragmento da Luz (4/4)")
    jogador.fragmentos.append("Fragmento da Lua Quebrada")
    print("A Cripta começa a tremer, como se a própria terra rejeitasse as trevas ali existentes.")
    print("Você foge por um túnel lateral enquanto o santuário desmorona, levando os horrores consigo.")

def torres_das_cinzas(jogador):
    print("O jogador parte para sua última missão, libertar o mundo das trevas e derrotar de uma vez por todas Malakar")
    print("Você adentra o santuário negro no topo da Torre das Cinzas.")
    print("Malakar surge das sombras, envolto em uma aura sombria e ameaçadora.")
    print('"Então você finalmente chegou, insolente..."')
    print('"Prepare-se para ser consumido pelas trevas eternas!"\n')
    print("Malakar levanta as mãos, conjurando um feitiço que consome sua energia vital.")
    print("Esqueletos surgem dos escombros, avançando para te atacar.")

    print("Malakar ergue uma barreira negra, tornando-se invulnerável!")
    print("Três fontes de escuridão surgem na sala, pulsando com energia maligna.")
    print("Você deve destruí-las para enfraquecer o necromante.")

    print("A barreira se desfaz, e Malakar ruge de fúria.")
    print("Ele conjura um ataque final devastador!")
    print("Mas você ergue o Coração da Luz, bloqueando as trevas com uma explosão de luz sagrada!")

    print("Malakar é derrotado, e a maldição começa a se dissipar das terras de Eltoria.")
    print("A luz retorna ao reino, e você é celebrado como um herói eterno.")
    print("Muito obrigado por ter jogado até aqui espero que tenha gostado!")
