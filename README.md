# 💬 Aplicação de Chatbot

Uma aplicação de chatbot baseada em Streamlit que utiliza ferramentas do Langchain e um gráfico de estado para fornecer respostas dinâmicas. O chatbot pode lidar com sinônimos, realizar cálculos e engajar em conversas gerais usando o modelo `llama-3.3-70b-versatile` via API Groq.

## Índice

- [Recursos](#recursos)
- [Pré-requisitos](#pr%C3%A9-requisitos)
- [Instalação](#instala%C3%A7%C3%A3o)
- [Configuração](#configura%C3%A7%C3%A3o)
- [Executando a Aplicação](#executando-a-aplica%C3%A7%C3%A3o)
- [Acessando o Chatbot](#acessando-o-chatbot)
- [Parando a Aplicação](#parando-a-aplica%C3%A7%C3%A3o)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Solução de Problemas](#solu%C3%A7%C3%A3o-de-problemas)

## Recursos

- **Ferramenta de Sinônimos**: Busca sinônimos para uma palavra fornecida.
- **Ferramenta de Calculadora**: Avalia expressões matemáticas simples.
- **IA Conversacional**: Engaja em conversas gerais usando um modelo de linguagem poderoso.
- **Gerenciamento de Estado**: Mantém o estado da conversa para interações coerentes.
- **Dockerizado**: Configuração e implantação fáceis usando Docker e Docker Compose.

## Pré-requisitos

Antes de começar, certifique-se de que você atendeu aos seguintes requisitos:

- **Git**: Para clonar o repositório.
- **Docker**: Para construir e executar os containers da aplicação.
- **Docker Compose**: Para gerenciar aplicações Docker com múltiplos containers.
- **Chave API da Groq**: Cadastre-se no [Groq](https://www.groq.com/) para obter sua chave API.

## Instalação

1.  **Clone o Repositório**

```bash
git clone https://github.com/henrisama/chatbot-groq.git
```

2.  **Navegue até o Diretório do Projeto**

```bash
cd chatbot-app
```

## Configuração

1.  **Configure as Variáveis de Ambiente**

    - **Copie o Arquivo de Exemplo de Ambiente**
      ```bash
      cp .env.example .env
      ```
    - **Configure a Chave API da Groq**

      Abra o arquivo `.env` no seu editor de texto preferido e adicione sua chave API da Groq

## Executando a Aplicação

1.  **Construa e Inicie os Containers**

    Certifique-se de que o Docker está rodando na sua máquina. Em seguida, execute o seguinte comando para construir e iniciar a aplicação:

    ```bash
    docker compose up
    ```

2.  **Aguarde a Inicialização da Aplicação**

    O Docker Compose irá baixar as imagens necessárias, instalar dependências e iniciar a aplicação Streamlit. Você deverá ver logs indicando que o servidor Streamlit está rodando na porta `8501`.

## Acessando o Chatbot

Uma vez que a aplicação esteja rodando, você pode acessar a interface do chatbot navegando para:

```arduino
http://localhost:8501`
```

Abra seu navegador web e vá para a URL acima para começar a interagir com o chatbot.

## Parando a Aplicação

Para parar os containers em execução, pressione `Ctrl + C` no terminal onde o Docker Compose está rodando. Para remover os containers, redes e outros recursos criados pelo Docker Compose, execute:

```bash
docker-compose down
```

## Estrutura do Projeto

```bash
chatbot-app/
│
├── src/
│   └── app.py            # Aplicação Streamlit
│   └── chatbot.py        # Lógica do Chatbot e ferramentas
├── .env.example          # Exemplo de variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo git
├── docker-compose.yml    # Configuração Docker Compose
├── Dockerfile            # Configuração Docker para a aplicação
├── README.md             # Documentação do projeto`
└── requirements.txt      # Dependências Python
```

## Solução de Problemas

- **Porta Já em Uso**

  Se a porta `8501` já estiver em uso, você pode alterar o mapeamento de portas no arquivo `docker-compose.yml`:

  ```yaml
  ports:
    - "8502:8501"
  ```

  Então, acesse a aplicação em `http://localhost:8502`.

- **Problemas com a Chave API**

  Certifique-se de que sua `GROQ_API_KEY` está corretamente configurada no arquivo `.env`. Chaves API ausentes ou incorretas impedirão o funcionamento adequado do chatbot.

- **Instalação do Docker**

  Verifique se o Docker e o Docker Compose estão corretamente instalados e em execução na sua máquina. Consulte a documentação oficial do Docker para guias de instalação.

## Observações Adicionais

- **Coloque** no arquivo `.env` a sua chave API real da Groq.
- **Certifique-se** de que todos os arquivos estejam na estrutura de diretórios correta conforme a [Estrutura do Projeto](#estrutura-do-projeto) no README.
