# URL Shortener - Encurtador de URLs

Uma aplicação web para encurtar URLs longas de forma rápida e simples. Perfeita para compartilhar links através de redes sociais, mensagens ou qualquer lugar onde URLs curtas sejam necessárias.

## Características

- **Encurtamento de URLs**: Converta URLs longas em endereços curtos e memoráveis
- **Aliases Personalizados**: Crie aliases customizados para seus URLs
- **Banco de Dados SQLite**: Armazenamento persistente de URLs e aliases
- **API REST**: Endpoints para gerenciar suas URLs encurtadas
- **Interface Web Intuitiva**: Frontend amigável para usuários

## Como Usar

### Instalação

1. Clone o repositório ou navegue até a pasta do projeto:

```bash
cd url-shortener
```

2. Instale as dependências:

```bash
pip install flask
```

3. Inicie a aplicação:

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

### Como Encurtar uma URL

#### Via Interface Web
1. Abra a interface web no navegador
2. Cole sua URL longa no campo de entrada
3. (Opcional) Defina um alias customizado
4. Clique em "Encurtar"
5. Compartilhe o link encurtado!

#### Via API

**POST /forms**
```bash
curl -X POST http://localhost:5000/forms \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://exemplo.com/pagina/muito/longa",
    "alias": "meu-link"
  }'
```

**Acessar URL Encurtada**
```
http://localhost:5000/meu-link
```

## Estrutura do Projeto

```
url-shortener/
├── app.py                    # Aplicação principal Flask
├── front.py                  # Interface frontend
├── db_url_shortener.db      # Banco de dados SQLite
└── README.md                # Este arquivo
```

## Tecnologias Utilizadas

- **Flask**: Framework web Python
- **SQLite**: Banco de dados leve e portátil
- **Python 3.x**: Linguagem de programação
- **HTML/CSS/JavaScript**: Frontend (em front.py)

## Estrutura do Banco de Dados

### Tabela: `urls`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `url` | TEXT | URL original longa |
| `alias` | TEXT UNIQUE | Alias curto e único |

## Endpoints da API

### POST /forms
Encurta uma URL

**Request:**
```json
{
  "url": "https://exemplo.com/pagina/muito/longa",
  "alias": "meu-link"
}
```

**Response:**
```json
{
  "status_code": 200,
  "alias": "meu-link",
  "short_url": "http://localhost:5000/meu-link"
}
```

### GET /<alias>
Redireciona para a URL original

**Resposta**: Redirecionamento 301 (Moved Permanently) para a URL original

## Exemplos de Uso

### Encurtar uma URL simples
```json
{
  "url": "youtube.com/watch?v=dQw4w9WgXcQ",
  "alias": "rick-roll"
}
```

Resultado: `http://localhost:5000/rick-roll`

### Encurtar com alias automático
Se nenhum alias for fornecido, um é gerado automaticamente com caracteres aleatórios.

## Configurações

- **Porta**: Padrão 5000
- **Banco de Dados**: SQLite (criado automaticamente)
- **Redirecionamento**: Usa código HTTP 301 (Moved Permanently)

## Segurança

- URLs são validadas antes de serem armazenadas
- Aliases únicos previnem conflitos
- Validação de protocolo (http/https)

## Troubleshooting

### URL não redireciona
- Verifique se o alias existe no banco de dados
- Certifique-se de que a URL original está válida
- Limpe o cache do navegador

### Erro ao criar alias
- O alias já pode estar em uso (use outro)
- Verifique a URL original
- Certifique-se que o servidor está rodando

## Melhorias Futuras

- [ ] Interface web mais moderna e responsiva
- [ ] Estatísticas de cliques por URL encurtada
- [ ] Expiração automática de URLs
- [ ] Autenticação de usuários
- [ ] Sistema de códigos QR
- [ ] Dashboard de gerenciamento
- [ ] Análise de origem do tráfego

## Contribuições

Contribuições são bem-vindas! Sinta-se livre para:
- Relatar bugs
- Sugerir novas funcionalidades
- Fazer melhorias no código

## Licença

Este projeto é de código aberto e disponível para fins educacionais e comerciais.

---

**Encurte seus URLs e compartilhe de forma simples!**
