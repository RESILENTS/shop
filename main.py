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
        callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)
        

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
            keyboard.add(callback_button)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь", reply_markup=keyboard)


bot.polling(none_stop=True)
