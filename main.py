import telebot 
import random
import time
import requests
import os

token = '1543845399:AAGMq9rrQW7xSvgAPnXUjpjBNVfw6G1E9HA'
bot = telebot.TeleBot(token)
ADMIN_CHAT_ID = 641892529

chat_ids_file = 'chat_ids.txt'

@bot.message_handler(commands=['start'])
def welcome(message):
    service = telebot.types.ReplyKeyboardMarkup(True)
    service.row('🛠 Инструменты', 'ℹ️ Канал бота')
    service.row('📊 Статистика', '🛒 Маркет')
    bot.send_message(message.chat.id, ('👋🏽 Добро пожаловать, *' + message.from_user.first_name + '.*'), reply_markup=service, parse_mode='Markdown')
    
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "📊 Статистика":
        with open('chat_ids.txt') as f:
            size = sum(1 for _ in f)
            bot.send_message(message.chat.id, '📊Статистика отображается в реальном времени📡!\nПользователей: ' + str(size) + '\nСервисов для RU🇷🇺: 30\nСервисов для UK🇺🇦: 30\nБот запущен: 29.03.2020')

    if message.text == "🛠 Инструменты":
        keyboard = telebo.types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="⚙️ BTCVoucherGen [2.0]:", url="https://t.me/BTC_CHANGE_BOT?start=с_" + new_pas)
        url2_button = types.InlineKeyboardButton(text="⚙️ QIWITokenGen&Check [1.0]", url="https://t.me/BTC_CHANGE_BOT?start=с_" + new_pas)
        keyboard.add(url_button, url2_button)
        bot.send_message(message.chat.id, "888", parse_mode='Markdown', disable_web_page_preview=True, reply_markup=keyboard)

        if message.text == "Dump DB" and chat_id == ADMIN_CHAT_ID:
            f = open('chat_ids.txt')
            bot.send_document(message.chat.id, f)
    
    
bot.polling(none_stop=True)
