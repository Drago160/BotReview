import telebot
from telebot import types
import src.config
from src.bot_engine import Engine
import PHRASES
import os
from flask import Flask, request
from src.dbParams import Client, RequestData

TOKEN = src.config.TOKEN
APP_URL = src.config.APP_URL 

bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)
engine = Engine()

clients = {} 

def register(my_id):
    clients[my_id] = Client(my_id)
    return clients[my_id] 


def logIn(id):
    if id in clients:
        return clients[id]
    else:
        return register(id)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, " + message.from_user.first_name)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, PHRASES.HELP_MESSAGE, parse_mode = 'HTML')

@bot.message_handler(commands=['find'])
def help(message):
    client = logIn(message.chat.id)
    client.askFlag = True
    bot.send_message(message.chat.id, PHRASES.WAIT_FOR_QUESTION, parse_mode = 'HTML')

@bot.message_handler(commands=['/changerules'])
def change(message):
    client = logIn(message.chat.id)
    bot.send_message(message.chat.id, PHRASES.HOW_MANY_QUEST, parse_mode = "HTML")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("1")
    button2 = types.KeyboardButton("2")
    markup.add(button1, button2)


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



def workError(message, client):
    Ans = engine.find_answer_on_error(message.text, client.reqData)
    for part in Ans:
        isQuestion = True
        for answer in part:
            if len(answer)>5:
                if isQuestion:
                    bot.send_message(message.chat.id, PHRASES.QUESTION, parse_mode = 'HTML')
                    isQuestion = False
                    isFirstAns = True
                else:
                    if isFirstAns:
                        bot.send_message(message.chat.id, PHRASES.ANSWER, parse_mode = 'HTML')
                        isFirstAns = False

                bot.send_message(message.chat.id, answer, parse_mode = 'HTML')
 


@bot.message_handler(content_types=['text'])
def lalala(message):

    client = logIn(message.chat.id)

    if client.askFlag:
        client.askFlag = False
        workError(message, client)

