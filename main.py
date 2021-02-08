import telebot
from telebot import types
import random
import time
import requests
import os
import ssl

token = '1543845399:AAGMq9rrQW7xSvgAPnXUjpjBNVfw6G1E9HA'
bot = telebot.TeleBot(token)
ADMIN_CHAT_ID = 641892529

chat_ids_file = 'chat_ids.txt'
auto_number_a = ''

marka = ''
region = ''
model = ''
zametki = ''
data_reg = ''
address = ''
year = ''

service = telebot.types.ReplyKeyboardMarkup(True)
service.row('🔍 Поиск данных', '⚙️ Инструменты')
service.row('ℹ️ FAQ', '📈 Канал')

@bot.message_handler(commands = ['start'])
def welcome(message):	
	bot.send_message(message.chat.id, '6 7', reply_markup=service, parse_mode='Markdown')
        
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "🔍 Поиск данных":  
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="🇺🇦 Украина", callback_data="uabtn")
        btn2 = types.InlineKeyboardButton(text="🇷🇺 Россия", callback_data="test")
        btn3 = types.InlineKeyboardButton(text="🇰🇿 Казахстан", callback_data="test")
        btn4 = types.InlineKeyboardButton(text="🇧🇾 Беларусь", callback_data="test")
        keyboard.add(btn1, btn2)
        keyboard.add(btn3, btn4)
        bot.send_message(message.chat.id, "🌐 Выберите нужную вам страну для поиска данных:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "uabtn":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="🔍 Поиск авто по гос номеру", callback_data="uabtn1_1")
            btn2 = types.InlineKeyboardButton(text="🔍 Поиск по номеру телефона", callback_data="test")
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
	
        if call.data == "uabtn1_1":
            service1 = telebot.types.ReplyKeyboardMarkup(True)
            service1.row('🔍 Поиск 🚙', '🏠 На главную')
            uabtn1_1_message = bot.send_message(chat_id=call.message.chat.id, text="🔍 Поиск информации о автомобиле по гос. номеру:\n\nℹ️ Отправь мне номер авто для проверки, пример номера *AA1234BB.*", reply_markup=service1, parse_mode='Markdown')
            bot.register_next_step_handler(uabtn1_1_message, auto_number_check)
	
		
	
def auto_number_check(message):
    global auto_number_a
    auto_number_a = message.text
    response = requests.get('https://fakescreen-3d98a1.eu1.kinto.io/ua?num=' + auto_number_a)
    data = response.json()
    region = data["region"]["name"]
    marka = data["vendor"]
    model = data["model"]
    year = data["year"]
    zametki = data["operations"][0]["notes"]
    data_reg = data["operations"][0]["regAt"]
    address = data["operations"][0]["address"]

    bot.send_message(message.chat.id, "🔍 Результат поиска по номеру: 🇺🇦*"+auto_number_a+"*\n\n▪️ Марка авто: " +marka+ "\n️▪️ Регион: " +region+ "\n▪️ Модель: " +model+ "\n▪️ Заметки: " +zametki+ "\n▪️ Дата последней регистрации: " + data_reg, parse_mode='Markdown')
        
bot.polling(none_stop=True)
