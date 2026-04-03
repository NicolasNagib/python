# RPG Eltoria - Jogo de Terminal

Um mini-jogo RPG interativo de terminal, desenvolvido em Python, que oferece uma experiência imersiva de decisões, combate e exploração em um mundo de fantasia.

## Características

- **Sistema de Classes**: Escolha entre Mago, Cavaleiro ou Bandido, cada um com atributos e habilidades únicas
- **Sistema de Combate**: Turnos estratégicos com ataque e defesa
- **Múltiplos Mundos**: Explore diversos locais como a Cripta da Lua, Torres das Cinzas e Templo da Chama Viva
- **Sistema de Inventário**: Colete itens e artefatos durante a jornada
- **Progressão de Personagem**: Ganhe XP e ouro ao derrotar inimigos
- **Inimigos Variados**: Enfrente diferentes adversários com diferentes atributos
- **Narrativa Interativa**: Histórias e diálogos que se adaptam às suas ações

## Como Jogar

### Instalação

1. Clone o repositório ou navegue até a pasta do projeto
2. Instale as dependências (se houver requirements.txt)
3. Execute o jogo:

```bash
cd rpg
python main.py
```

### Como Iniciar

1. Digite seu nome de personagem quando solicitado
2. Escolha sua classe:
   - **Mago**: Alta inteligência, baixa defesa, uso de magia
   - **Cavaleiro**: Alta defesa, ataque moderado, resistência
   - **Bandido**: Alta agilidade, ataques rápidos, baixa defesa
3. Explore o mundo, enfrente inimigos e saia vitorioso!

## Estrutura do Projeto

```
rpg/
├── main.py                 # Ponto de entrada do jogo
├── requisitos.md          # Especificações do jogo
├── game/
│   ├── engine.py          # Motor principal do jogo
│   ├── combat.py          # Sistema de combate
│   └── world.py           # Definição dos mundos e locais
├── entities/
│   ├── classesPersonagens.py  # Classes dos personagens
│   ├── player.py          # Entidade do jogador
│   └── enemy.py           # Entidade de inimigos
├── data/
│   ├── enemies.json       # Dados dos inimigos
│   └── listaAtaques.py    # Lista de ataques disponíveis
└── funcoes/
    └── fala.py            # Funções de diálogo e narrativa
```

## Sistemas do Jogo

### Atributos do Personagem
- **HP (Vida)**: Pontos de saúde do personagem
- **Ataque**: Dano causado ao adversário
- **Defesa**: Redução de dano recebido
- **XP (Experiência)**: Progresso para melhorias
- **Ouro**: Moeda do jogo

### Sistema de Combate
- Turnos alternados entre jogador e inimigo
- Escolha entre ataque físico, defesa ou habilidade especial
- Combate termina quando um dos lados tem zero HP

### Exploração
- Navegue por diferentes mundos
- Descubra artefatos e itens especiais
- Derrote inimigos para obter recompensas

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal
- **OOP (Programação Orientada a Objeto)**: Estrutura de classes

## Detalhes de Desenvolvimento

Este projeto foi desenvolvido com o objetivo de:
- Aprender e praticar Programação Orientada a Objeto em Python
- Criar um sistema de jogo funcional com múltiplos componentes
- Implementar mecânicas interativas de RPG

## Status do Projeto

**Em Desenvolvimento** - Novas funcionalidades e melhorias estão sendo adicionadas

### Funcionalidades Planejadas
- Sistema de equipamentos e upgrades
- Mais classes e habilidades especiais
- Sistema de magia mais elaborado
- Boss fights
- Save/Load de progresso

## Contribuições

Sinta-se livre para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar melhorias

## Licença

Este projeto é de código aberto e disponível para fins educacionais.

---

**Divirta-se explorando o mundo de Eltoria!** 
