from config import *
import random
import telebot
from telebot import types


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_message(message):

    if message.text[:6] == 'Привет'.lower():
        bot.send_message(message.from_user.id, 'Привет. Твой гороскоп на сегодня.')

        keyboard = types.InlineKeyboardMarkup()

        for i in range(len(zodiaks)):
            key = types.InlineKeyboardButton(text=zodiaks[i], callback_data='zodiac' + zodiaks[i])
            keyboard.add(key)

        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака.', reply_markup=keyboard)

    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши "Привет".')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши - "/help".')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data[:6] == 'zodiac':
        msg = f'{call.data[6:]}:\n{random.choice(first)} {random.choice(second)} {random.choice(second_add)} {random.choice(third)}'
        bot.send_message(call.message.chat.id, msg)      
