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
    join_btn = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='➕ Присоединиться к каналу', url='t.me/shadowbchat')
    join_btn.add(btn_my_site)
    bot.send_message(message.chat.id, "🤖* BTCVoucherGen 2.0:* Генератор BTC чеков. Скрипт генерирует ссылки для обнала BTC чеков в Telegram ботах.\n\n🔐 Что-бы получить доступ к боту вам нужно подписаться на наш канал.", parse_mode='Markdown', reply_markup=start_kb)

bot.polling(none_stop=True)
