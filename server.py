from zodiak import bot
from flask import Flask


app = Flask(__name__)

@app.route('/')
def run_bot():
    bot.polling(none_stop=True, interval=0)
    return 'Bot is runing....'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
