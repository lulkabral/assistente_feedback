#Assistente de Feedback Textual

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

cliente = Groq()


def contar_palavras(texto_do_aluno):
   texto2 =  texto_do_aluno.split()
   palavras_unicas = set(texto2)
   return len(texto2),len(palavras_unicas)
 
meu_texto = input("Cole seu texto para análise: ")

def analisador_gramatica(meu_texto): 
   resposta = cliente.chat.completions.create(
       model = "openai/gpt-oss-120b",
       messages = [
          {"role": "system", "content": "You are a grammar analyzer. You will analyze the text provided by the user and provide feedback on grammar, spelling, and punctuation errors. Please provide suggestions for improvement."},
          {"role": "user", "content": meu_texto}
      ]
       
)
   return resposta.choices[0].message.content


total_palavras, palavras_unicas = contar_palavras(meu_texto)
feedback_ia = analisador_gramatica(meu_texto)

relatorio = f"""
=========================================
RELATÓRIO DE FEEDBACK PEDAGÓGICO
=========================================
Estatísticas do Texto:
- Palavras totais: {total_palavras}
- Palavras únicas: {palavras_unicas}

AVALIAÇÃO DA IA:
{feedback_ia}
=========================================
"""

print(relatorio)