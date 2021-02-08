import telebot
from telebot import types
import random
import time
import requests
from grab import Grab
import os
from bs4 import BeautifulSoup as BS

token = '1543845399:AAGMq9rrQW7xSvgAPnXUjpjBNVfw6G1E9HA'
bot = telebot.TeleBot(token)
ADMIN_CHAT_ID = 641892529

chat_ids_file = 'chat_ids.txt'
d = ''


service = telebot.types.ReplyKeyboardMarkup(True)
service.row('🔍 Начать поиск')
service.row('ℹ️ FAQ', '📈 Канал')


@bot.message_handler(commands = ['start'])
def welcome(message):
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36","Connection": "keep-alive","Host": "iknowwhatyoudownload.com","Referer": "https://iknowwhatyoudownload.com"}
			page = requests.get("https://iknowwhatyoudownload.com/ru/peer/?ip=93.170.136.172", headers=headers)
			soup = BS(page.content, "html.parser")
			table = soup.find(class_="table").find("tbody")
			torrents = table.find_all("tr")
			for torrent in torrents:
				first, last = torrent.find_all(class_="date-column")
				first, last = first.text, last.text
				category = torrent.find(class_="category-column").text
				name = torrent.find(class_="name-column").text.replace("\n", '').replace('    ', '')
				size = torrent.find(class_="size-column").text
			bot.send_message(message.chat.id, '6 ' + category, reply_markup=service, parse_mode='Markdown')
        
@bot.message_handler(func=lambda message: True, content_types=['text'])
def any_msg(message):
    if message.text == "🔍 Начать поиск":  
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="🇺🇦 Украина", callback_data="uabtn")
        btn2 = types.InlineKeyboardButton(text="🇷🇺 Россия", callback_data="test")
        btn3 = types.InlineKeyboardButton(text="🇰🇿 Казахстан", callback_data="test")
        btn4 = types.InlineKeyboardButton(text="🇧🇾 Беларусь", callback_data="test")
        btn5 = types.InlineKeyboardButton(text="⚙️ Разные OSINT инструменты", callback_data="otherosint")
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
            
        if call.data == "otherosint":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="👥 Генератор фейк данных", callback_data="otherosint_1")
            keyboard.add(btn1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="⚙️ Выберите нужный вам инструмент.", reply_markup=keyboard)

        if call.data == "otherosint_1":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="🧑‍ Женский", callback_data="otherosint_1_1")
            btn2 = types.InlineKeyboardButton(text="👨‍ Мужской", callback_data="otherosint_1_2")
            keyboard.add(btn1,btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👥 Генератор фейк данных:\n\nВыберите нужный вам пол для генерации данных.", reply_markup=keyboard)

        if call.data == "otherosint_1_1":
            url = "https://randomuser.me/api/"
            response = requests.get(url).json()
            gender = "male"
            name = response["results"][0]["name"]
            location = response["results"][0]["location"]
            birthday = response["results"][0]["dob"]
                        
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="🧑‍ Женский", callback_data="otherosint_1_1")
            btn2 = types.InlineKeyboardButton(text="👨‍ Мужской", callback_data="otherosint_1_2")
            keyboard.add(btn1,btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👥 Генератор фейк данных:\n\nВыберите"+{birthday['date']}+" нужный вам пол для генерации данных.", reply_markup=keyboard)

        
bot.polling(none_stop=True)
