from zodiak import bot
from flask import Flask


app = Flask(__name__)

@app.route('/')
def bot_start():
    return 'Bot is runing....'


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
