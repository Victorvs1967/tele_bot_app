from zodiak import bot
from flask import Flask


app = Flask(__name__)

@app.route('/')
def bot_start():
    bot.polling(none_stop=True, interval=0)
    return 'Bot is runing....'
