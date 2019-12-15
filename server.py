from config import TOKEN, HEROKU_APP_URL
from zodiak import *
from flask import Flask, request
import os


app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok!", 200
  
@app.route('/', methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url=HEROKU_APP_URL + TOKEN)
    return '<h2>Runing zodiac bot...</h2>', 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
