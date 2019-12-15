from zodiak import bot
from flask import Flask
import os


app = Flask(__name__)
flag = True

@app.route('/')
def bot_start():
    return '<h2>Bot is runing...</h2><a href="/bot">Bot</a>', 200

@app.route('/bot')
def bot_run():
    global flag
    if flag:
        bot.polling(none_stop=True, interval=0)
        flag = False
    return 'Bot is starting....', 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
