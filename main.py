import src.bot
import os

if __name__ == '__main__':
    src.bot.server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
TOKEN = "5271610100:AAGe5hpOOwyp4oqF1qMrLXzth5fobbGZoEA"

