import telebot
import config
from src.bot_engine import Engine
import PHRASES
import os
from flask import Flask, request
from src.dbParams import Client, RequestData

TOKEN = config.TOKEN
APP_URL = config.APP_URL 

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
    if engine.define(message):
        Ans = engine.find_answer_on_error(message.text)
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
