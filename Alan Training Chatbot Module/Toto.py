from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from sklearn import linear_model

import os

bot = ChatBot('Toto')
bot.set_trainer(ListTrainer)

for files in os.listdir('G:/Project/Toto in Python/data/english/'):
    #G:/Project/Toto in Python/data/english/
    data = open('G:/Project/Toto in Python/data/english/' + files, 'r').readlines()
    bot.train(data)

while True:
    message = input('You:')
    if message.strip != 'Bye':
        reply = bot.get_response(message)
        print('TOTO : ', reply)
    if message.strip() == 'Bye':
        print('TOTO : Bye')
        break

#lr = linear_model.LogisticRegression()
#lr.fit(data)
#lr.score(data)
