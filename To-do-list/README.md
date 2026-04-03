# To-Do List - Gerenciador de Tarefas

Uma aplicação web moderna para gerenciar suas tarefas do dia a dia. Com uma interface intuitiva e funcionalidades poderosas, mantém você produtivo e organizado.

## Características

- **Adicionar Tarefas**: Crie novas tarefas com facilidade
- **Marcar como Concluído**: Controle o progresso das suas tarefas
- **Deletar Tarefas**: Remova tarefas que não são mais necessárias
- **Avisos de Duplicação**: O sistema avisa se você está criando uma tarefa duplicada
- **Data de Criação**: Cada tarefa registra automaticamente quando foi criada
- **Interface Responsiva**: Design que funciona em diferentes tamanhos de tela
- **Backend Robusto**: API REST bem estruturada com Flask
- **Banco de Dados Persistente**: Seus dados são salvos em SQLite

## Como Usar

### Instalação

1. Clone o repositório ou navegue até a pasta do projeto:

```bash
cd To-do-list
```

2. Crie e ative um ambiente virtual:

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux/Mac
python -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Iniciando a Aplicação

1. **Inicie o servidor Flask** (novo terminal):

```bash
python app.py
```

O servidor estará disponível em `http://localhost:5000`

2. **Inicie a interface web** (outro terminal, com o ambiente virtual ativado):

```bash
streamlit run front.py
```

A interface abrirá automaticamente em `http://localhost:8501`

## Estrutura do Projeto

```
To-do-list/
├── app.py                  # Backend Flask - API REST
├── front.py                # Frontend Streamlit - Interface Web
├── requirements.txt        # Dependências do projeto
├── db_toDoList.db         # Banco de dados SQLite (criado automaticamente)
├── routes/
│   └── post.py            # Rotas e handlers adicionais (opcional)
└── README.md              # Este arquivo
```

## Tecnologias Utilizadas

- **Flask**: Framework web backend Python
- **Streamlit**: Framework para interface web interativa
- **SQLite**: Banco de dados leve e portátil
- **Python 3.x**: Linguagem de programação
- **Python-requests**: Para fazer requisições HTTP

## Estrutura do Banco de Dados

### Tabela: `itemsList`

| Coluna | Tipo | Descrição | Padrão |
|--------|------|-----------|--------|
| `ROWID` | INTEGER | ID único da tarefa | Auto-incrementado |
| `title` | TEXT | Título/descrição da tarefa | - |
| `completed` | BOOL | Status se foi completada | FALSE |
| `create_date` | DATE | Data de criação | Data atual |

## Endpoints da API (Backend)

### POST /
Cria uma nova tarefa

**Request:**
```json
{
  "title": "Fazer compras"
}
```

**Response:**
```json
{
  "status_code": 200
}
```

**Status Codes:**
- `200`: Tarefa criada com sucesso
- `208`: Tarefa já existe (duplicada)
- `400`: Erro na requisição

### POST /addRepeatItem
Adiciona uma tarefa duplicada (com permissão do usuário)

**Request:**
```json
{
  "title": "Fazer compras"
}
```

**Response:**
```json
{
  "status_code": 200
}
```

### PUT /deleteTask/<id>
Deleta uma tarefa pelo ID

**Response:**
```json
{
  "status_code": 200
}
```

### GET /getTasks
Recupera todas as tarefas

**Response:**
```json
[
  {
    "id": 1,
    "title": "Fazer compras",
    "completed": false,
    "create_date": "2024-04-03"
  }
]
```

### PUT /markCompleted/<id>
Marca uma tarefa como concluída

**Response:**
```json
{
  "status_code": 200
}
```

## Como Usar a Aplicação

### Adicionar uma Tarefa
1. Digite a tarefa no campo de entrada
2. Clique em "Adicionar Tarefa"
3. Se a tarefa já existe, você será notificado
4. Escolha se deseja adicioná-la mesmo assim

### Marcar como Concluído
1. Clique no checkbox ao lado da tarefa
2. A tarefa será marcada como completa
3. A interface se atualiza automaticamente

### Deletar uma Tarefa
1. Clique no botão "Deletar" ao lado da tarefa
2. Confirme a exclusão no diálogo
3. A tarefa será removida da lista

## Interface Streamlit

A interface oferece:
- **Layout limpo e intuitivo**: Fácil de usar para qualquer pessoa
- **Feedback em tempo real**: Atualizações instantâneas
- **Diálogos informativos**: Confirmação de ações importantes
- **Responsivo**: Funciona em desktop, tablet e mobile
- **Toast notifications**: Mensagens de feedback sobre ações

## Dependências

Ver [requirements.txt](requirements.txt):

- Flask: Web framework
- Streamlit: Interface interativa
- requests: Requisições HTTP

## Segurança

- Validação de entrada de dados
- Prevenção de SQL Injection através de prepared statements
- Status codes HTTP apropriados
- Tratamento de erros adequado

## Troubleshooting

### "Erro de conexão com o servidor"
- Certifique-se de que o Flask está rodando (`python app.py`)
- Verifique se a porta 5000 está disponível
- Reinicie ambos os serviços

### "Tarefa não aparece na lista"
- Atualize a página (F5)
- Verifique se o servidor do Flask está respondendo
- Limpe o cache do navegador

### "Erro ao instalar dependências"
- Certifique-se de que o Python 3.6+ está instalado
- Atualize o pip:
```bash
python -m pip install --upgrade pip
```
- Tente instalar novamente:
```bash
pip install -r requirements.txt
```

## Dicas de Uso

- Mantenha seus títulos curtos e descritivos
- Use diferentes níveis de prioridade (não há campo, mas você pode usar emojis)
- Revise suas tarefas regularmente
- Delete tarefas concluídas para manter a lista limpa

## Melhorias Futuras

- [ ] Categorias/tags para tarefas
- [ ] Prioridades (Alta, Média, Baixa)
- [ ] Datas de vencimento
- [ ] Lembretes por email
- [ ] Autenticação de usuários
- [ ] Listas compartilhadas
- [ ] Estatísticas de produtividade
- [ ] Tema escuro/claro
- [ ] Backup automático
- [ ] API mais completa (GET, UPDATE)

## Contribuições

Contribuições são bem-vindas! Você pode:
- Relatar bugs
- Sugerir novas funcionalidades
- Melhorar a interface
- Otimizar o código

## Licença

Este projeto é de código aberto e disponível para fins educacionais e pessoais.

---

**Mantenha-se produtivo com sua lista de tarefas!**
