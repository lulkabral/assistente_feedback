# Assistente de Feedback Textual 

Um assistente pedagógico inteligente construído em Python que usa a API do Groq (modelo Meta Llama 3) para analisar textos, contar métricas e dar feedback gramatical detalhado.

Atualmente funcionando via terminal, o projeto está em transição para se tornar uma aplicação web interativa com um avatar visual focado no apoio direto aos alunos.

## Funcionalidades Atuais (Terminal)
* **Análise Léxica:** Contagem de palavras totais e palavras únicas a partir do texto do usuário.
* **Correção Inteligente:** Avaliação de gramática, ortografia e pontuação através de Inteligência Artificial generativa.
* **Sugestões Estilísticas:** Recomendações de vocabulário e estrutura de frases para melhoria contínua.
* **Segurança:** Gestão de credenciais isolada e protegida através de variáveis de ambiente (.env).

## Roadmap e Próximos Passos 🚀
- [ ] **Migração Back-end:** Transformar o script Python em uma API web usando FastAPI e Uvicorn.
- [ ] **Interface Front-end:** Construir a interface visual no navegador usando React + Vite.
- [ ] **Agente Visual:** Desenhar e integrar um mascote/avatar interativo para guiar a experiência de correção.

## Como Executar Localmente

1. Clone este repositório:
`git clone https://github.com/SEU_USUARIO/assistente_feedback.git`

2. Acesse a pasta do projeto e ative o seu ambiente virtual:
`cd assistente_feedback` e depois `source .venv/bin/activate`

3. Instale as dependências:
`pip install groq python-dotenv fastapi uvicorn`

4. Crie um arquivo .env na raiz do projeto e adicione a sua chave da API do Groq:
`GROQ_API_KEY="sua_chave_aqui"`

5. Execute o assistente:
`python3 assistente.py`