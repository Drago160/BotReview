import src.bot
import os

if __name__ == '__main__':
    src.Bot.server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
