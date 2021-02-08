import telebot
from telebot import types
from telebot import Message
import random
import time
import requests
import os
import ssl

token = '1543845399:AAGMq9rrQW7xSvgAPnXUjpjBNVfw6G1E9HA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
  sent = bot.send_message(message.chat.id, 'Please describe your problem.')
  bot.register_next_step_handler(sent, hello)

def hello(message):
    open('problem.txt', 'w').write(message.chat.id + ' | ' + message.text + '||')
    bot.send_message(message.chat.id, 'Thank you!')
    bot.send_message(ADMIN_ID, message.chat.id + ' | ' + message.text)
	
bot.polling(none_stop=True)
