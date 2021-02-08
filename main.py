import telebot
from telebot import types
import random
import time
import requests
from bs4 import BeautifulSoup
import os

token = '1543845399:AAGMq9rrQW7xSvgAPnXUjpjBNVfw6G1E9HA'
bot = telebot.TeleBot(token)
ADMIN_CHAT_ID = 641892529

chat_ids_file = 'chat_ids.txt'
d = ''

service = telebot.types.ReplyKeyboardMarkup(True)
service.row('🔍 Начать поиск')
service.row('ℹ️ FAQ', '📈 Канал')


@bot.message_handler(commands=['start'])
def welcome(message):
    for j in range(1):
        #указываем url и get параметры запроса
        url = 'https://baza-gai.com.ua/nomer/CE1234BC'
        # указываем get параметр с помощью которого определяется номер страницы
        par = {'p': j}
        # записываем ответ сервера в переменную r
        r = requests.get(url, params=par)
        # получаем объект  BeautifulSoup и записываем в переменную soup
        soup = BeautifulSoup(r.text, 'html.parser')
        # с помощью циклам перебераем товары на странице и получаем из них нужные параметры
        for i in range(20):
               # получаем название товара
               product = soup.find_all('<div><strong>Реєстрація:</strong>')[i].get_text()
               # получаем цену товара
               price = soup.find_all(class_='price_g')[i].get_text()
               # удаляем пробел из цены
               print(product)
            
    bot.send_message(message.chat.id, ('👋🏽 Добро пожаловать, *' + message.from_user.first_name + '.*'), reply_markup=service, parse_mode='Markdown')
        
@bot.message_handler(func=lambda message: True, content_types=['text'])
def any_msg(message):
    if message.text == "🔍 Начать поиск":  
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="🇺🇦 Украина", callback_data="uabtn")
        btn2 = types.InlineKeyboardButton(text="🇷🇺 Россия", callback_data="test")
        btn3 = types.InlineKeyboardButton(text="🇰🇿 Казахстан", callback_data="test")
        btn4 = types.InlineKeyboardButton(text="🇧🇾 Беларусь", callback_data="test")
        btn5 = types.InlineKeyboardButton(text="⚙️ Разные OSINT инструменты", callback_data="test")
        keyboard.add(btn1, btn2)
        keyboard.add(btn3, btn4)
        keyboard.add(btn5)
        bot.send_message(message.chat.id, "🌐 Выберите нужную вам страну для поиска данных:", reply_markup=keyboard)
        
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "uabtn":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="🔍 Поиск по Государственному Номеру", callback_data="uabtn")
            btn2 = types.InlineKeyboardButton(text="🔍 Поиск по Номеру Телефона", callback_data="test")
            keyboard.add(btn1)
            keyboard.add(btn2)
            
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🇺🇦 Все доступные инструменты для поиска нужной вам информации.", reply_markup=keyboard)
            
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=pogoda1, text="Пыщь2")


bot.polling(none_stop=True)
