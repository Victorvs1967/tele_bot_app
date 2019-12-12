import random
import telebot
from telebot import types


first = ['Сегодня идеальный день для новых начинаний.', 'Оптимальный день для того, чтобы решиться на смелый поступок!', 'Будьте осторожны, сегодня звезды могут повлиять на ваше финансовое состояние.', 'Лучшее время, чтобы разобраться со старыми отношениями или начать новые.', 'Плодотворный день для того, чтобы разобраться с накопившимися делами.']

second = ['Но помините, что даже в этом случае не нужно забывать про', 'Те, кто сегодня нацелен выполнить много дел, должны помнить про', 'Если у вас упадок сил, обратите внимание на', 'Помните, что мысли материальны, а значит в течении дня нужно постоянно думать про']

second_add = ['отношения с друзьями и длизкими.', 'работу и деловые вопросы, которые могут так не кстати помешать планам.', 'себя и свое здоровье, иначе к вечеру возможен полный раздрай.', 'бытовые вопросы - особенно те, которые не сделали вчера.', 'отдых, чтобы не превратить себя в загнанную лошадь к концу месяца.']

third = ['Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.', 'Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.', 'Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дело до конца.', 'не нужно бояться одиноких встречь - сегодня то самое время, когда они значат многое.', 'Усли встретите незнакомца на пути - проявите участие, и тогда эта встреча посулит вам приятные хлопоты.']

zodiaks = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']

TOKEN = '801617964:AAGG_uN1V2hb3jWps0fSeEJuaykEfY632xA'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_message(message):

    if message.text[:6] == 'Привет':
        bot.send_message(message.from_user.id, 'Привет. Твой гороскоп на сегодня.')

        keyboard = types.InlineKeyboardMarkup()

        for i in range(len(zodiaks)):
            key = types.InlineKeyboardButton(text=zodiaks[i], callback_data='zodiac')
            keyboard.add(key)

        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака.', reply_markup=keyboard)

    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши "Привет".')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши - "/help".')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == 'zodiac':
        msg = f'{random.choice(first)} {random.choice(second)} {random.choice(second_add)} {random.choice(third)}'
        bot.send_message(call.message.chat.id, msg)      


if __name__ == "__main__":
    
    bot.polling(none_stop=True, interval=0)
