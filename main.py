import telebot
from telebot import types
import random
import time
import requests
import os
import ssl

token = '1543845399:AAGMq9rrQW7xSvgAPnXUjpjBNVfw6G1E9HA'
bot = telebot.TeleBot(token)
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == '🔎 OSINT':
        username_check = bot.send_message(message.from_user.id, 'Введите регистрационный номер:')
        bot.register_next_step_handler(username_check, get_car_model)

def get_car_model(message):
    global username_check_a
    username_check_a = message.text.upper()
    expire = usernameSearch(message.from_user.id)
    bot.send_message(message.from_user.id, twitter_i)

def usernameSearch(self): 
    global username_check_a
    
    twitterurl = 'https://twitter.com/' + username_check_a
    twitterresponse = get(twitterurl, headers=headers)
    if twitterresponse.status_code == 200:
        twitter_i = bot.send_message(message.from_user.id, ' ❌ *Twitter:* Не найдено.', parse_mode='Markdown')
    else:
        twitter_i = bot.send_message(message.from_user.id, ' ➖ *Twitter:* https://twitter.com/' + username_check_a, parse_mode='Markdown')
