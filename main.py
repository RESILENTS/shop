import telebot
from telebot import types
import random
import time
import requests
import os
import ssl

username = ''

token = '1543845399:AAGMq9rrQW7xSvgAPnXUjpjBNVfw6G1E9HA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
  sent = bot.send_message(message.chat.id, 'Please describe your problem.')
  bot.register_next_step_handler(sent, hello)

def hello(message):
    global username
    username = message.text
    bot.send_message(message.chat.id, 'Thank you!')
    bot.send_message(message.chat.id, '657567' + username)
	
bot.polling(none_stop=True)
