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
tel_number_a = ''

marka = ''
region = ''
model = ''
zametki = ''
data_reg = ''
address = ''
year = ''


@bot.message_handler(commands = ['start'])
def welcome(message):	
        service = telebot.types.ReplyKeyboardMarkup(True)
        service.row('🔍 Поиск данных', '⚙️ Инструменты')
        service.row('ℹ️ Руководство', '🛠 Наши проекты')
        bot.send_message(message.chat.id, "👋🏽 Добро пожаловать, *"+ message.from_user.first_name +".**\n\nТЕНЕВОЙ ПОИСК — Я помогу тебе с поиском информации.*\n\nУ меня есть функции для поиска информации по интернету.\nДанный проект работает на абсолютно бесплатной основе и создан ради того, чтобы помочь вам в поисках лиц.\n\n👤 *По всем вопросам: @resilents*", reply_markup=service, parse_mode='Markdown')
        
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
        bot.send_message(message.chat.id, "🌐 *Выберите нужную вам страну для поиска данных:* \n\n*«Пробив»* — это противоправная услуга, с помощью которой злоумышленники получают из закрытых баз данных информацию о конкретном человеке или организации. Естественно, за деньги. Существование такого предложения было бы невозможно без инсайдеров — сотрудников, у которых есть доступ к нужной информации для выполнения служебных обязанностей.", reply_markup=keyboard, parse_mode='Markdown')

    if message.text == "⚙️ Инструменты":  
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="🔩 Генераторы", callback_data="uabtn")
        btn2 = types.InlineKeyboardButton(text="⛓ Чекеры", callback_data="test")
        btn3 = types.InlineKeyboardButton(text="📢 Спам, Флуд", callback_data="test")
        btn4 = types.InlineKeyboardButton(text="🔨 Разные", callback_data="test")
        keyboard.add(btn1, btn2)
        keyboard.add(btn3, btn4)
        bot.send_message(message.chat.id, "🌐 *Выберите нужную вам страну для поиска данных:* \n\n*«Пробив»* — это противоправная услуга, с помощью которой злоумышленники получают из закрытых баз данных информацию о конкретном человеке или организации. Естественно, за деньги. Существование такого предложения было бы невозможно без инсайдеров — сотрудников, у которых есть доступ к нужной информации для выполнения служебных обязанностей.", reply_markup=keyboard, parse_mode='Markdown')
	
    if message.text == "🏠 На главную":  
        service = telebot.types.ReplyKeyboardMarkup(True)
        service.row('🔍 Поиск данных', '⚙️ Инструменты')
        service.row('ℹ️ FAQ', '📈 Канал')
        bot.send_message(message.chat.id, "🌐 Выберите нужную вам страну для поиска данных:", reply_markup=service)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "uabtn":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="🔍 Поиск авто по гос номеру", callback_data="uabtn1_1")
            btn2 = types.InlineKeyboardButton(text="🔍 Поиск по номеру телефона", callback_data="uabtn1_2")
            keyboard.add(btn1)
            keyboard.add(btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🇺🇦 Все доступные инструменты для поиска нужной вам информации.", reply_markup=keyboard)  

        if call.data == "uabtn1_2":
            uabtn1_1_message = bot.send_message(chat_id=call.message.chat.id, text="🔍 Поиск информации о автомобиле по гос. номеру:\n\nℹ️ Отправь мне номер авто для проверки, пример номера *AA1234BB.*", parse_mode='Markdown')
            bot.register_next_step_handler(uabtn1_1_message, auto_number_check)
		
        if call.data == "uabtn1_1":
            uabtn1_2_message = bot.send_message(chat_id=call.message.chat.id, text="🔍 Поиск информации о автомобиле по гос. номеру:\n\nℹ️ Отправь мне номер авто для проверки, пример номера *AA1234BB.*", parse_mode='Markdown')
            bot.register_next_step_handler(uabtn1_2_message, getcontact)
	
def getcontact():
    global tel_number_a
    tel_number_a = message.text
    req = requests.get("https://phonebook.space/?input=+" + tel_number_a, headers={"Cookie": "__atuvc=3%7C44%2C4%7C45; __atuvs=5f9e30e7193af6a7003"})
    soup = BeautifulSoup(req.content, 'lxml')
    for result in soup.select("div.results > ul"):
    bot.send_message(message.chat.id, result.get_text().replace(" ", ""))
		
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
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="🔍 Новый поиск", callback_data="uabtn1_1")
    keyboard.add(btn1)
    bot.send_message(message.chat.id, "*🔍 Результат поиска по гос номеру: "+auto_number_a+"*\n\n▪️ *Марка авто:* " +marka+ "\n️▪️ *Регион:* " +region+ "\n▪️ *Модель:* " +model+ "\n▪️ *Заметки:* " +zametki+ "\n▪️ *Дата последней регистрации:* " + data_reg, reply_markup=keyboard, parse_mode='Markdown')
        
bot.polling(none_stop=True)
