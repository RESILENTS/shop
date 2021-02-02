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
service.row('🛠 Инструменты', 'ℹ️ Канал бота')
service.row('📊 Статистика', '🛒 Маркет')

service2 = telebot.types.ReplyKeyboardMarkup(True)
service2.row('⚙️ Генераторы', '🔍 OSINT')
service2.row('📥 Парсеры', '🔗 Разные')
service2.row('🏠 Перейти на главную')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, ('👋🏽 Добро пожаловать, *' + message.from_user.first_name + '.*'), reply_markup=service, parse_mode='Markdown')
    
@bot.message_handler(commands=['btcvouchergen'])
def any_msg(message):
    service3 = telebot.types.ReplyKeyboardMarkup(True)
    service3.row('🤖 Chatex Bot', '🤖 BTC Banker')
    service3.row('🏠 Перейти на главную')
    bot.send_message(message.chat.id, "🤖* BTCVoucherGen 2.0:* Генератор BTC чеков. Скрипт генерирует ссылки для обнала BTC чеков в Telegram ботах.", reply_markup=service3, parse_mode='Markdown')
        
@bot.message_handler(commands=['qiwitools'])
def qiwitools(message):
    service4 = telebot.types.ReplyKeyboardMarkup(True)
    service4.row('⚙️ Сгенерировать', '🏠 Перейти на главную')
    bot.send_message(message.chat.id, "🤖* BTCVoucherGen 2.0:* Генератор BTC чеков. Скрипт генерирует ссылки для обнала BTC чеков в Telegram ботах.", reply_markup=service4, parse_mode='Markdown')
        
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "📊 Статистика":
        with open('chat_ids.txt') as f:
            size = sum(1 for _ in f)
            bot.send_message(message.chat.id, '📊Статистика отображается в реальном времени📡!\nПользователей: ' + str(size) + '\nСервисов для RU🇷🇺: 30\nСервисов для UK🇺🇦: 30\nБот запущен: 29.03.2020')

    if message.text == "🏠 Перейти на главную":
        bot.send_message(message.chat.id, ('👋🏽 Добро пожаловать, *' + message.from_user.first_name + '.*'), reply_markup=service, parse_mode='Markdown') 
            
    if message.text == "🛠 Инструменты":
        bot.send_message(message.chat.id, ('👋🏽 Добро пожаловать, *' + message.from_user.first_name + '.*'), reply_markup=service2, parse_mode='Markdown') 
        
    if message.text == "⚙️ Генераторы":
        bot.send_message(message.chat.id, ('/btcvouchergen | *BTCVoucherGen:* Генератор BTC чеков.\n/qiwitools | *QIWITokenGen:* Генерируем QIWI Token и чекаем.'), reply_markup=service2, parse_mode='Markdown') 
        
    if message.text == "🤖 BTC Banker":
        new_pas = Functions.btc_banker()
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Открыть ссылку", url="https://t.me/BTC_CHANGE_BOT?start=с_" + new_pas)
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "🤖 *БОТ:* [BTC Banker.](https://t.me/BTC_CHANGE_BOT)\n🔗 *Чек:* `" + new_pas + "`", parse_mode='Markdown', disable_web_page_preview=True, reply_markup=keyboard)
        
    if message.text == "⚙️ Сгенерировать":
        new_pas2 = Functions.qiwi_gen()
        token = new_pas2
        session = requests.Session()
        session.headers['Accept']= 'application/json'
        session.headers['authorization'] = 'Bearer ' + token
            try:
                req = session.get("https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true").json()
                bot.send_message(message.chat.id, "+", parse_mode='Markdown',new_pas2, disable_web_page_preview=True)
                    except:
                bot.send_message(message.chat.id, "-", parse_mode='Markdown',new_pas2, disable_web_page_preview=True)
            except:

    if message.text == "🤖 Chatex Bot":
        new_pas = Functions.chatex()
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Открыть ссылку", url="https://t.me/Chatex_bot?start=c_" + new_pas)
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "🤖 *БОТ:* [Chatex_bot.](https://t.me/Chatex_bot)\n🔗 *Чек:* `" + new_pas + "`", parse_mode='Markdown', disable_web_page_preview=True, reply_markup=keyboard)


bot.polling(none_stop=True)
