from zodiak import bot
from flask import Flask
import os


app = Flask(__name__)
flag = False

@app.route('/')
def bot_start():
    return 'Bot is runing....', 200

@app.route('/run')
def bot_run():
    if flag:
        return 'Bot is runing....'
    bot.polling(none_stop=True, interval=0)
    flag = True


if __name__ == "__main__":
    pass
# bot.polling(none_stop=True, interval=0)
# app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
