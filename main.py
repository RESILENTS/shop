import telebot
from telebot import types
import random
import time
import requests
import os
import Functions
from SimpleQIWI import *

token = '1543845399:AAGMq9rrQW7xSvgAPnXUjpjBNVfw6G1E9HA'
bot = telebot.TeleBot(token)
ADMIN_CHAT_ID = 641892529

chat_ids_file = 'chat_ids.txt'

service = telebot.types.ReplyKeyboardMarkup(True)
service.row('🔍 Начать поиск')
service.row('ℹ️ FAQ', '📈 Канал')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, ('👋🏽 Добро пожаловать, *' + message.from_user.first_name + '.*'), reply_markup=service, parse_mode='Markdown')
        
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "🔍 Начать поиск":  
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="🇺🇦 Украина", callback_data="uabtn")
        btn2 = types.InlineKeyboardButton(text="🇷🇺 Россия", callback_data="test")
        keyboard.add(btn1, btn2)
        bot.send_message(message.chat.id, "🌐 Выберите нужную вам страну для поиска данных:", reply_markup=keyboard)
        
def callback_inline(call):
    if call.message:
        if call.data == "uabtn":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="🇺🇦 Поиск по гос номеру", callback_data="test")
            btn2 = types.InlineKeyboardButton(text="🇺🇦 Поиск по номеру телефона", callback_data="test")
            btn3 = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
            btn4 = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
            keyboard.add(btn1)
            keyboard.add(btn2)
            keyboard.add(btn3, btn4)
            bot.send_message(message.chat.id, "🔍 Выберите нужный вам режим для поиска данных:", reply_markup=keyboard)


bot.polling(none_stop=True)
