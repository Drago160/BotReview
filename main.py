import telebot
import config
from src.bot_engine import Engine

bot = telebot.TeleBot(config.TOKEN)
engine = Engine()

@bot.message_handler(content_types=['text'])
def lalala(message):
    if engine.define(message):
        Ans = engine.find_answer_on_error(message.text)
    for answer in Ans:
        if len(str(answer))>3:
            answer = str(answer)
            #answer = "["+answer+"](" + "https://stackoverflow.com/questions/33757661/how-could-you-increase-the-maximum-recursion-depth-in-python" + ")"
            bot.send_message(message.chat.id, answer, parse_mode='markdown')

#RUN
bot.polling(none_stop=True)

