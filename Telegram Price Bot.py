# pip install requests
# pip install pyTelegramBotAPI

import telebot
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
    'Content-Type': 'application/json',
}
# To create a Telegram bot, you can use Botfather in Telegram, place the bot token here, start the bot, run the project, and press /start. That's it :)
API_TOKEN = 'YOUR_API_TOKEN_HERE'  # Replace with your actual API token
bot = telebot.TeleBot(API_TOKEN)
url = 'https://price.tlyn.ir/api/v1/price'
response = requests.get(url, headers=headers)
prices = response.json()['prices']
buttons = {
    "Gold Gram 18K": None,
    "Mithqal 17K": None,
    "Full Coin": None,
    "Half Coin": None,
    "Quarter Coin": None
}
def get_price(price_title):
    for price in prices:
        if price['title'] == price_title:
            sell_price = price['price']['sell'] * 1000  # Convert to Rial
            buy_price = price['price']['buy'] * 1000    # Convert to Rial
            return f"{price_title}:\n\nSell: {sell_price:,} Toman\nBuy: {buy_price:,} Toman"


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons:
        markup.add(button)
    bot.send_message(message.chat.id, "Hello! Please select the desired button:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text in buttons:
        price_message = get_price(message.text)
        bot.send_message(message.chat.id, price_message)

bot.polling()
