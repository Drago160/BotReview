import src.bot
import os

if __name__ == '__main__':
    if src.bot.Heroku_running_flag:
        src.bot.server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        src.bot.bot.polling(none_stop=True)
