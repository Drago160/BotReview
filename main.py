import telebot
import config
from src.bot_engine import Engine
import PHRASES
import os
from flask import Flask, request
from src.dbParams import Client, RequestData

TOKEN = "5360585147:AAFADUTSH1xYFcZrVV-0fNWkgsVQic6HxiE"
APP_URL = f'https://reviewshybot.herokuapp.com/{TOKEN}'

bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)
engine = Engine()

Clients = {} 

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, " + message.from_user.first_name)

@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


def register(my_id):
    clients[my_di] = Client()
    return clients[my_id] 


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.from_user.id in clients:
        client = clients[message.from_user.id]
    else:
        client = register(message.from_user.id) 
    if engine.define(message):
        Ans = engine.find_answer_on_error(message.text, client.reqData)
        for part in Ans:
            isQuestion = True
            for answer in part:
                if len(answer)>2:
                    if isQuestion:
                        bot.send_message(message.chat.id, PHRASES.QUESTION, parse_mode = 'HTML')
                        isQuestion = False
                        isFirstAns = True
                    else:
                        if isFirstAns:
                            bot.send_message(message.chat.id, PHRASES.ANSWER, parse_mode = 'HTML')
                            isFirstAns = False

                    bot.send_message(message.chat.id, answer, parse_mode = 'HTML')
#bot.polling(none_stop=True)

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
