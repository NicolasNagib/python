from funcoes.fala import fala


def descobrir_artefatos(jogador):
    texto_artefatos = [
        "Após decidir isso você sai em busca do arqueólogo da cidade, ele conta que os artefatos estão protegidos em quatro templos: "
        "Templo da chama viva: um local que já serviu como centro de guia espiritual, mas que hoje é ocupado por um culto, que realiza sacrifícios humanos, esperando que as trevas se dissipem, e assim a luz retorne"
        "Nivel recomendado: 10"
        "Templo congelado de Elgran: este lugar é protegido pelo espírito de Elgran, um dragão de gelo maligno, que congelou as terras ao redor do templo, onde hoje elas abrigam golens de gelo, e o terrível Yeti"
        "Nivel recomendado: 20"
        "Ruínas submersas do templo de Nymor: Lugar onde outrora abrigava incriveis criaturas marinhas, hoje é o esconderijo do Kraken, a criatura mais poderosa dos oceanos"
        "Nivel recomendado: 25, Relíquia necessária: Benção das águas"
        "Cripta da Lua quebrada: Lugar onde Malakar evoluiu seus poderes, antigamente este lugar era um santuário dedicado a deusa Lunala"
        "Nivel recomendado: 30"
        "Após descobrir mais sobre o lugar, o guerreiro ganha um mapa onde ele pode escolher para onde ir"
    ]
    fala(texto_artefatos)
    jogador.mapa = True

def descobrir_torre(jogador):
    texto_descobrir_torre = [
        "O guerreiro se encontra com o ancião da vila, o ancião conta que Malakar está absorvendo as almas das pessoas para se fortalecer, também conta que a torre oculta é o esconderijo de Malakar, mas explica que não recomenda ir lá sem o artefato, pois sem ele o guerreiro será consumido pelas trevas"
    ]
    jogador.alarme_torre = True
    fala(texto_descobrir_torre)
    
def templo_chama_viva(jogador):
    texto_templo_chama = [
        "Você se aproxima do Templo da Chama Viva, um antigo santuário agora consumido por trevas e fanatismo.",
        "Chamas altas dançam nas torres do templo. O calor é sufocante. O ar cheira a enxofre e madeira queimada.",
        "Ao chegar à entrada, você é observado por olhos ocultos entre as colunas de pedra negra.",
        "De repente, três sacerdotes maníacos surgem — suas túnicas estão em chamas, mas eles parecem não sentir dor.",
        "Sacerdote: 'Mais um tolo em busca da luz perdida... Você será o próximo sacrifício!'",
        "\nVocê se prepara para o combate!",
        # (aqui você pode chamar: combate.combate(jogador, sacerdote1), etc.)
        
        "\nApós derrotar os fanáticos, você entra no templo em ruínas."
        "O chão está repleto de símbolos gravados em sangue e brasas acesas por todo o salão."
        "No centro do templo, um altar flamejante queima com fogo eterno — e sobre ele, uma figura sombria observa em silêncio."

        "É o Guardião da Chama — outrora protetor da luz, agora corrompido pela promessa do poder eterno."
        "Guardião: 'Eu protejo o fragmento da luz... Mas não para você. Prove-se digno ou queime!'"

        "\nVocê se prepara para enfrentar o Guardião da Chama."

    # (aqui: combate final - ex: combate.combate(jogador, guardiao_chama))

        "\nCom muito esforço, você derrota o Guardião."
        "As chamas ao redor do altar diminuem e revelam o 1º Fragmento da Luz."
        "Você sente uma energia pura e poderosa preencher seu corpo."
        "Você obteve: Fragmento da Luz (1/4)"

        "Ao deixar o templo, você escuta uma voz ecoando nas paredes:"
        "'Os outros fragmentos esperam... Mas a escuridão também.'"

        "Sua jornada continua..."
    ]
    jogador.fragmentos.append("Fragmento da Chama Viva")
    fala(texto_templo_chama)
    
def templo_elgran(jogador):
    texto_templo_elgran = [
        "Você parte rumo ao norte, onde os ventos são cortantes e a neve nunca derrete."
        "Após dias de viagem por vales gelados e rios congelados, você avista a entrada do Templo Congelado de Elgran."
        "Esculturas de dragões adornam o portão, cobertas por gelo grosso. O silêncio é absoluto, como se o próprio tempo estivesse congelado ali."
        "Ao entrar, o frio é tão intenso que congela sua respiração. Você sente sua energia sendo drenada lentamente."
        "De repente, criaturas começam a emergir do chão de gelo... são Golens de Gelo, guardiões antigos do templo!"

        "\nVocê entra em combate contra os Golens de Gelo!"

    # Exemplo: combate.combate(jogador, golem1)

        "\nAo derrotá-los, você avança por um salão onde espelhos de cristal refletem sua imagem de maneira distorcida."
        "No fim do corredor, um santuário antigo guarda uma fonte congelada — e nela, um espírito feminino de aparência etérea."

        "Espírito: 'Você é corajoso. Antes que enfrente Elgran, receba minha bênção.'"
        "Ela toca sua testa e você sente uma energia aquática percorrer seu corpo."

        "Você recebeu: **Benção das Águas**"
        "Com ela, você poderá respirar e se mover livremente nas profundezas das Ruínas de Nymor."

        "Você encontra inscrições nas paredes — histórias perdidas de Elgran, o Dragão de Gelo que selava os espíritos das tempestades."
        "Mais adiante, uma ponte de gelo suspensa leva até um altar de gelo azul brilhante."
        "Mas antes de chegar ao fim, um rugido profundo ecoa pelas paredes do templo..."

        "Elgran desperta de seu sono milenar!"

        "Elgran: 'Você ousa pisar neste santuário sagrado? O frio eterno será sua prisão!'"
        "O dragão de gelo colossal se ergue entre estalactites congeladas, com olhos brilhando como safiras."
        "Você não tem escolha: precisa enfrentá-lo para recuperar o segundo fragmento!"

        "\nCombate épico contra Elgran, o Dragão de Gelo!"

    # Exemplo: combate.combate(jogador, elgran)

        "\nApós um confronto árduo, você derrota Elgran."
        "Seu corpo congela em cristais de gelo puro e se desfaz em pó brilhante."
        "No centro do altar, protegido por runas antigas, repousa o segundo Fragmento da Luz."
        "Você sente uma onda gélida de poder fluir até seu coração."

        "Você obteve: Fragmento da Luz (2/4)"
        
        "O templo começa a ruir, como se seu propósito tivesse sido cumprido."

        "Você corre para fora antes que tudo desmorone."
        "Do alto da montanha congelada, observa ao longe... ainda restam dois fragmentos, e a jornada está longe do fim."
    ]
    fala(texto_templo_elgran)
    jogador.fragmentos.append("Fragmento de Elgran")

def ruinas_submersas(jogador):
    texto_ruinas_submersas = [
        
        "Você parte em direção ao sul, onde o mar encontra os pântanos e os ventos carregam o cheiro de sal e podridão."
        "As águas estão escuras, e a maré parece recuar ao sentir sua aproximação."
        "Graças à Benção das Águas, você respira fundo e mergulha..."

        "Você adentra um abismo submerso, onde a luz desaparece rapidamente."
        "No fundo do oceano, encontra estruturas antigas cobertas por corais e algas. As Ruínas de Nymor, esquecidas por séculos."

        "Enquanto explora os corredores submersos, sombras se movem ao seu redor..."
        "Sirenas corrompidas sussurram melodias mortais, tentando te atrair para armadilhas."
        "Você se vê obrigado a lutar."

    # Exemplo:
    # combate.combate(jogador, sirena1)

        "Após escapar do encanto das sirenas, você chega a uma praça circular submersa."
        "Uma grande escadaria de pedra leva a uma cripta selada com símbolos antigos do mar."

        "Você encosta a mão e os símbolos brilham com a energia da Benção das Águas."
        "A passagem se abre... e uma corrente forte te suga para o fundo."

        "Você acorda em uma câmara escura, com colunas destruídas e conchas gigantes presas nas paredes."
        "O chão começa a tremer... e então, os tentáculos do **Kraken** surgem da escuridão."

        "Kraken: 'Você ousa perturbar o sono do abismo? Que os mares silenciem sua alma.'"

        "Inicia-se o combate contra o Kraken — o maior guardião do templo."

    # combate.combate(jogador, kraken)

        "A batalha é brutal. O Kraken ataca com tentáculos gigantes, jatos d'água e tenta te puxar para as profundezas."
        "Mas após muita resistência, ele solta um último rugido aquático e se desfaz em espuma abissal."

        "No centro da arena, um altar se ergue com o **Terceiro Fragmento da Luz**, flutuando em uma bolha de água pura."

        "Você obteve: Fragmento da Luz (3/4) "
        "A água ao redor se purifica, e as ruínas parecem respirar pela primeira vez em séculos."
        "Você retorna à superfície, sentindo-se mais forte... mas também mais próximo do fim."
    ]
    jogador.fragmentos.append("Fragmento de Nymor")
    fala(texto_ruinas_submersas)

def cripta_lua(jogador):
    texto_cripta_lua_pt1 = [
            "Você segue rumo às montanhas esquecidas, onde o céu parece mais pesado e a lua raramente brilha."
            "Após atravessar cavernas de pedras negras e florestas mortas, você encontra uma entrada semi-soterrada por ossos e símbolos distorcidos."
            "A Cripta da Lua Quebrada... outrora um santuário de luz, agora apodrecido pelo toque das trevas."

            "Ao adentrar, você sente um frio que não vem do vento, mas da própria alma do lugar."
            "Nas paredes, inscrições lunares foram riscadas, manchadas com sangue e transformadas em runas de necromancia."

            "Vultos sussurram nos corredores. Espíritos corrompidos da antiga ordem da deusa Lunala surgem."
            "Eles foram convertidos em guardiões mortos-vivos por Malakar."

            "Você precisa enfrentá-los para continuar."

        # combate.combate(jogador, espectro1)

            "Com as almas libertadas, um dos espectros aponta para uma porta selada com símbolos lunares partidos."
            "Você precisa resolver um enigma para abri-la..."

            "Enigma: 'Sou a luz que não brilha, a sombra que ilumina. Quando caio, tudo dorme. Quem sou eu?'"
        ]
    fala(texto_cripta_lua_pt1)
    resposta = input(fala("Sua resposta: ")).strip().lower()

    if resposta in ["lua", "a lua"]:
        texto_cripta_lua_pt2= ["Os símbolos brilham brevemente com luz prateada. A porta se abre."]
        fala(texto_cripta_lua_pt2)
    else:
        texto_cripta_lua_pt2 = [
            "Nada acontece. Uma força te empurra para trás. Você tenta novamente até acertar."
            # Poderia repetir ou forçar combate adicional

            "Atravessando a porta, você encontra um salão circular com vitrais quebrados e um altar negro."
            "No centro, uma figura encapuzada, de costas para você, murmura palavras sombrias."

            "??? : 'A Deusa da Lua os abandonou... mas eu? Eu os ouvi. Eu dei poder a eles.'"
            "O ser se vira — é um antigo sacerdote, agora completamente deformado pela magia negra."

            "Sacerdote Caído: 'Não deixarei que leve a última centelha de luz.'"

            "Inicia-se o combate contra o **Sacerdote da Lua Corrompido**!"

        # combate.combate(jogador, sacerdote)

            "O sacerdote ataca com feitiços lunares corrompidos, invoca almas e manipula a escuridão para confundir você."
            "Mas ao ser derrotado, ele olha para o céu, e por um segundo... a lua ressurge através de uma fresta no teto."

            "Uma última luz ilumina o altar. Você caminha até ele e encontra o **último Fragmento da Luz**."

            "Você obteve: Fragmento da Luz (4/4)"
            "A Cripta começa a tremer, como se a própria terra rejeitasse as trevas ali existentes."
            "Você foge por um túnel lateral enquanto o santuário desmorona, levando os horrores consigo."]
        jogador.fragmentos.append("Fragmento da Lua Quebrada")
        fala(texto_cripta_lua_pt2)

def torres_das_cinzas(jogador):
   texto_torre_das_cinzas = [
       
        "O jogador parte para sua última missão, libertar o mundo das trevas e derrotar de uma vez por todas Malakar"
        "Você adentra o santuário negro no topo da Torre das Cinzas."
        "Malakar surge das sombras, envolto em uma aura sombria e ameaçadora."
        '"Então você finalmente chegou, insolente..."'
        '"Prepare-se para ser consumido pelas trevas eternas!"\n'
        "Malakar levanta as mãos, conjurando um feitiço que consome sua energia vital."
        "Esqueletos surgem dos escombros, avançando para te atacar."

        "Malakar ergue uma barreira negra, tornando-se invulnerável!"
        "Três fontes de escuridão surgem na sala, pulsando com energia maligna."
        "Você deve destruí-las para enfraquecer o necromante."

        "A barreira se desfaz, e Malakar ruge de fúria."
        "Ele conjura um ataque final devastador!"
        "Mas você ergue o Coração da Luz, bloqueando as trevas com uma explosão de luz sagrada!"

        "Malakar é derrotado, e a maldição começa a se dissipar das terras de Eltoria."
        "A luz retorna ao reino, e você é celebrado como um herói eterno."
        "Muito obrigado por ter jogado até aqui espero que tenha gostado!"
   ] 
   
   fala(texto_torre_das_cinzas)