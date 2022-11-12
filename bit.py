import requests
import telebot
from datetime import datetime
from auth_data import token
from telebot import types



# def get_data():
#     req = requests.get('https://yobit.net/api/3/ticker/btc_rur')
#     response = req.json()
#     sell_price = response["btc_rur"]["sell"]
#     print(f"{datetime.now().strftime('%Y-%m-%d-%H:%H')}\nSell BTC price: {sell_price}")


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn = types.KeyboardButton('Price')
        markup.add(btn)
        bot.send_message(message.chat.id, "Hello, bro, let's find out what the price of BTC", reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'price':
            try:
                req = requests.get('https://yobit.net/api/3/ticker/btc_rur')
                response = req.json()
                sell_price = response["btc_rur"]["sell"]
                bot.send_message(message.chat.id,
                                 f"{datetime.now().strftime('%Y-%m-%d-%H:%M')}\nSell BTC price to ruble: {sell_price}")
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id,'Damn...something gone wrong :(')
        else:
            bot.send_message(message.chat.id, 'Check the command!')
    bot.polling(none_stop=True)


if __name__ == '__main__':
    # get_data()
    telegram_bot(token)



