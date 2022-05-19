import telebot
from telebot import types
import src.config
from src.botEngine import Engine
import PHRASES
import os
from flask import Flask, request
from src.dbParams import Client, RequestData

TOKEN = src.config.TOKEN
APP_URL = src.config.APP_URL 

bot = telebot.TeleBot(TOKEN)

engine = Engine()

clients = {} 

#Клава с кнопочками вспомогательными
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttonStart = types.KeyboardButton("start")
buttonFind = types.KeyboardButton("find")
buttonChangeRule = types.KeyboardButton("changerule")
buttonHelp = types.KeyboardButton("help")
markup.add(buttonStart, buttonFind, buttonChangeRule, buttonHelp)

#Клава с кнопочками цифр
inputMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("1")
button2 = types.KeyboardButton("2")
button3 = types.KeyboardButton("3")
button4 = types.KeyboardButton("4")
button5 = types.KeyboardButton("5")
inputMarkup.add(button1, button2, button3, button4, button5)

def register(my_id):
    """Регистрирует пользователя локально"""
    clients[my_id] = Client(my_id)
    return clients[my_id] 

def logIn(id):
    """Проверяет зарегистрирован ли юзер,
    если нет - регистрирует"""
    if id in clients:
        return clients[id]
    else:
        return register(id)

@bot.message_handler(commands=['start'])
def start(message):
    """команда start"""
    bot.reply_to(message, "Hello, " + message.from_user.first_name, reply_markup = markup)

@bot.message_handler(func = lambda message: message.text == "start")
def to_start(message):
    """Кнопка start"""
    start(message)

@bot.message_handler(commands=['help'])
def helper(message):
    """Команда /help"""
    bot.send_message(message.chat.id, PHRASES.HELP_MESSAGE, reply_markup = markup, parse_mode = 'HTML')

@bot.message_handler(func = lambda message: message.text == "help")
def to_helper(message):
    """Кнопка help"""
    helper(message)

@bot.message_handler(commands=['find'])
def find(message):
    """Команда /find"""
    client = logIn(message.chat.id)
    client.askFlag = True
    bot.send_message(message.chat.id, PHRASES.WAIT_FOR_QUESTION, parse_mode = 'HTML')

@bot.message_handler(func = lambda message: message.text == "find")
def to_find(message):
    """Кнопка find"""
    find(message)

@bot.message_handler(commands=['changerule'])
def change(message):
    """Команда /changerule"""
    client = logIn(message.chat.id)
    bot.send_message(message.chat.id, PHRASES.HOW_MANY_QUEST, reply_markup = inputMarkup, parse_mode = "HTML")
    client.howManyQuestFlag = True

@bot.message_handler(func = lambda message: message.text == "changerule")
def to_change(message):
    """Кнопка changerule"""
    change(message)

def searchRequest(message, client):
    """Находим Ответы по запросу"""
    bot.send_message(message.chat.id, PHRASES.BEFORE, parse_mode="HTML")
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
                bot.send_message(message.chat.id, answer, reply_markup = markup, parse_mode = 'HTML')
 
@bot.message_handler(content_types=['text'])
def takeMessage(message):
    """Получаем сообщение в телеге"""
    client = logIn(message.chat.id)

    if client.askFlag:
        searchRequest(message, client)
        client.askFlag = False
    elif client.howManyQuestFlag:
        if not client.updateQuestNum(message.text):
            pass 
        else:
            bot.send_message(message.chat.id, PHRASES.SUCCESS_QUEST_MESSAGE, parse_mode="HTML")

    elif client.howManyAnsFlag: 
        if not client.updateAnsNum(message.text):
            pass 
        else:
            bot.send_message(message.chat.id, PHRASES.SUCCESS_ANS_MESSAGE, reply_markup = markup, parse_mode = "HTML")



#Тут мы смотрим если это Хероку, то делаем Webhook, иначе локально поллинг

if "HEROKU" in list(os.environ.keys()):

    server = Flask(__name__)

    @server.route('/' + TOKEN, methods=['POST'])
    def get_message():
        """Получение сообщения"""
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '!', 200

    @server.route('/')
    def webhook():
        """Вебхук"""
        bot.remove_webhook()
        bot.set_webhook(url=APP_URL)
        return '!', 200
    Heroku_running_flag = True
else:
    bot.remove_webhook()
    Heroku_running_flag = False 

