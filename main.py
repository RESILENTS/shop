import telebot 
import random
import time
import requests
import os

token = '1543845399:AAGMq9rrQW7xSvgAPnXUjpjBNVfw6G1E9HA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    service = telebot.types.ReplyKeyboardMarkup(True)
    service.row('ℹ Информация ', '🚀 Запустить')
    service.row('📊 Статистика', '💰 Премиум')
    service.row('📞 Поддержка', '👤 Профиль')
    bot.send_message(message.chat.id, ('👋🏽 Добро пожаловать, *' + message.from_user.first_name + '.*'), reply_markup=service, parse_mode='Markdown')
    
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "📊 Статистика":
        with open('chat_ids.txt') as f:
            size = sum(1 for _ in f)
            bot.send_message(chat_id, '📊Статистика отображается в реальном времени📡!\nПользователей: ' + str(size) + '\nСервисов для RU🇷🇺: 30\nСервисов для UK🇺🇦: 30\nБот запущен: 29.03.2020')
    
bot.polling(none_stop=True)
