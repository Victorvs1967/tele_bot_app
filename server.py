from zodiak import bot
from flask import Flask
import os


app = Flask(__name__)

@app.route('/')
def bot_start():
    return 'Bot is runing....', 200

@app.route('/run')
def bot_run():
    bot.polling(none_stop=True, interval=0)
    return 'Bot is runing....'


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)

app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
