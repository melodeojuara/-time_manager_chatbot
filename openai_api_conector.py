!pip install openai
!pip install python-dotenv

import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = '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'
completion = openai.Completion()
print(openai.api_key)

def chatbot(question, chat_log = None):
  if chat_log is None:
    chat_log = start_chat_log
    
    prompt = f'{chat_log}Human: {question}\nAi:'
    response = completion.create(prompt  = prompt,
                                 engine = 'ChatGPT',
                                 stop = ['\nHuman'],
                                 temperature = 0.9,
                                 top_p = 1,
                                 frequency_penalty = 0,
                                 presence_penalty = 0.6,
                                 best_of = 1,
                                 max_tokens = 150)
    resposta = response.choices[0].text.strip()
  return resposta

question = ' '
while question != '':
  question = input()
  print(chatbot(question))
