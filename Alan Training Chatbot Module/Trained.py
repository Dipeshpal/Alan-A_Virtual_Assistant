from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Toto')
bot.set_trainer(ListTrainer)

while True:
    message = input('You:')
    if message.strip != 'Bye':
        reply = bot.get_response(message)
        print('TOTO : ', reply)
    if message.strip() == 'Bye':
        print('TOTO : Bye')
        break
