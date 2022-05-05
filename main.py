import telebot
import config
from src.bot_engine import Engine
import PHRASES

bot = telebot.TeleBot(config.TOKEN)
engine = Engine()

@bot.message_handler(content_types=['text'])
def lalala(message):
    if engine.define(message):
        Ans = engine.find_answer_on_error(message.text)
        for part in Ans:
            isQuestion = True
            for answer in part:
                if len(answer)>3:
                    if isQuestion:
                        bot.send_message(message.chat.id, PHRASES.QUESTION, parse_mode = 'HTML')
                        isQuestion = False
                        isFirstAns = True
                    else:
                        if isFirstAns:
                            bot.send_message(message.chat.id, PHRASES.ANSWER, parse_mode = 'HTML')
                            isFirstAns = False

                    bot.send_message(message.chat.id, answer, parse_mode = 'HTML')
#RUN
bot.polling(none_stop=True)

