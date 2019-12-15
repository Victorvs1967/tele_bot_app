from zodiak import bot
from flask import Flask
import os


app = Flask(__name__)
flag = False

@app.route('/')
def bot_start():
    global flag
    if flag:
        return 'Bot is runing....', 200
    bot.polling(none_stop=True, interval=0)
    flag = True
    return 'Bot is starting....', 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
