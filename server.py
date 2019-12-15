from config import TOKEN, HEROKU_APP_URL
from zodiak import *
from flask import Flask, request
import os


app = Flask(__name__)
flag = True

# @app.route('/')
# def bot_start():
#     return '<h2>Bot is runing...</h2>', 200

@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
  
@app.route('/', methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url=HEROKU_APP_URL + TOKEN)
    return "Hello from Heroku!", 200

# @app.route('/bot')
# def bot_run():
#     global flag
#     if flag:
#         bot.polling()
#         # bot.polling(none_stop=True, interval=0)
#         flag = False
#     return 'Bot is starting....', 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
