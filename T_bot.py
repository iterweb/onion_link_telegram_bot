#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import telebot
from telebot import types
import random
import time
import hosting, sundry, finance, forum, search_onion, emaill, infos

bot_speak = ['Ок. Я передам это Сноудену!', 'Спасибо за сообщение, Мы с Эдвардом рассмотрим твоё редложение!', 'Голубь с твоим сообщением уже в пути...']
bot_sreak_move_to = ['Значит смотрим далее...', 'Вперёд так вперёд!']
bot_sreak_move_back = ['Ок. Давай варнёмся!', 'Назад!']

faqs = '/add_text и далее твоё сообщение или ссылка на ресурс (с кратким описанием)\nНапример: /add_text Добавь этот сайт www.sait.com, он очень крутой.\nИ я передам твоё сообщение Эдварду!\n\n/start - запус\n/reload - перезагрузка'
supports = 'Как ты можешь поддержать проект?\n\nБольшой поддержкой для меня, с твоей стороны, будет, если ты просто расскажешь своим друзьям, обо мне!'


URL         = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=html'
TOKEN       = '' # токен бота
CHANNELID   = '' # ссылка на канал, например: @my_chanel

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
            message.chat.id,
                '''Привет, Друг✌\nМеня зовут... Хотя, не зовут... Ты сам меня нашёл 😉\nМне дали имя Матрикс, не знаю почему так, наверное потому, что я знаком с Эдвардом Сноуденом и храню его секреты о всемирном заговоре и глобальной слежке.\n\nА может ты избранный, как Нео и попал ко мне не случайно?!
		''')
    time.sleep(5)
    bot.send_photo(message.chat.id, open('m.jpg', 'rb')) 
    time.sleep(3)
    bot.send_message(message.chat.id, 'И так, каков твой выбор?', reply_markup=choices())

@bot.message_handler(content_types=["text"])
def send_anytext(message):  
    #user = message.text.lower()
    chat_id = message.chat.id
    if message.text == 'Красная':
        bot.send_message(message.from_user.id, 'Я твой путеводитель на тёмной стороне интернета!\nСсылки обновляются раз в неделю (если, есть чем обновлять).', reply_markup=keyboard())
    elif message.text == 'Синяя':
        bot.send_message(message.from_user.id, 'Это твой выбор, как знаешь!\nhttps://www.google.com/')  
    elif message.text == 'Поиск':
        bot.send_message(chat_id, search_onion.site_SO,reply_markup=keyboard())
    elif message.text == 'Хостинг':
        bot.send_message(chat_id, 'Список на услуги хостинга',reply_markup=hostings())
    elif message.text == 'Форум':
        bot.send_message(chat_id, 'Выбирай',reply_markup=forums())
    elif message.text == 'Разное':
        bot.send_message(chat_id, sundry.site_S,reply_markup=move_to())
    elif message.text == 'Финансы':
        bot.send_message(chat_id, 'Список сайтов финансовой тематики',reply_markup=finances())
    elif message.text == '👈 Назад':
        bot.send_message(chat_id, random.choice(bot_sreak_move_back), reply_markup=keyboard())
    elif message.text == '<<=':
        bot.send_message(chat_id, random.choice(bot_sreak_move_back),reply_markup=keyboard())
    elif message.text == '<<==':
        bot.send_message(chat_id, random.choice(bot_sreak_move_back),reply_markup=keyboard())        
    elif message.text == '<<<==':
        bot.send_message(chat_id, random.choice(bot_sreak_move_back),reply_markup=keyboard())        
    elif message.text == 'Услуги Хостинга':
        bot.send_message(chat_id, hosting.site_H,reply_markup=hostings())
    elif message.text == 'Веб-дизайн':
        bot.send_message(chat_id, hosting.site_H1,reply_markup=hostings()) 
    elif message.text == 'Cервис изображений':
        bot.send_message(chat_id, hosting.site_H2,reply_markup=hostings()) 
    elif message.text == 'Файловые сервисы':
        bot.send_message(chat_id, hosting.site_H3,reply_markup=hostings())
    elif message.text == 'Список 1':
        bot.send_message(chat_id, forum.site_list1,reply_markup=forums())
    elif message.text == 'Список 2':
        bot.send_message(chat_id, forum.site_list2,reply_markup=forums())
    elif message.text == 'Список 3':
        bot.send_message(chat_id, forum.site_list3,reply_markup=forums())
    elif message.text == 'Миксера':
        bot.send_message(chat_id, finance.site_mixer,reply_markup=finances())
    elif message.text == 'Обменники':
        bot.send_message(chat_id, finance.site_exchage,reply_markup=finances())
    elif message.text == 'Кошельки':
        bot.send_message(chat_id, finance.site_wallet,reply_markup=finances())
    elif message.text == 'ИНФО':
        bot.send_message(chat_id, infos.inform,reply_markup=info_to())
    elif message.text == 'Поддержка':
        bot.send_message(chat_id, supports,reply_markup=info_to())
    elif message.text == 'FAQ':
        bot.send_message(chat_id, faqs,reply_markup=info_to())
    elif message.text == 'Почта':
        bot.send_message(chat_id, emaill.site_mail,reply_markup=move_to())        
    elif message.text == 'Вперёд 👉':
        bot.send_message(chat_id, random.choice(bot_sreak_move_to),reply_markup=move_to())  
    elif message.text == '👈 Нaзад':
        bot.send_message(chat_id, random.choice(bot_sreak_move_back), reply_markup=keyboard())
    elif user.startswith('/add_text'):
            requests.get(URL % (TOKEN, CHANNELID, user.replace('/add_text','')))
            bot.send_message(message.from_user.id, random.choice(bot_speak))
    elif user.startswith('/reload'):
            bot.send_message(message.from_user.id, 'Перезагрузка выполнена', reply_markup=keyboard())            
    else:
        bot.send_message(chat_id, 'Что ты имеешь ввиду? Вот список моих команд:')
        bot.send_message(chat_id, faqs)
def choices():
    markup1 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    blue_b = types.KeyboardButton('Синяя')
    red_b = types.KeyboardButton('Красная')
    markup1.add(red_b, blue_b)
    return markup1

def move_to():
    markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    back_to = types.KeyboardButton('👈 Назад')
    sundry = types.KeyboardButton('Разное')
    post = types.KeyboardButton('Почта')
    markup2.add(back_to, post, sundry)
    return markup2

def info_to():
    markup3 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    back_to_move_to = types.KeyboardButton('👈 Нaзад')
    faq = types.KeyboardButton('FAQ')
    support = types.KeyboardButton('Поддержка')
    markup3.add(back_to_move_to, support, faq)
    return markup3

def hostings():
    markup3 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    back_to = types.KeyboardButton('<<=')
    host = types.KeyboardButton('Услуги Хостинга')
    w_des = types.KeyboardButton('Веб-дизайн')
    image = types.KeyboardButton('Cервис изображений')
    file_ser = types.KeyboardButton('Файловые сервисы')
    markup3.add(host, w_des, image, back_to, file_ser)
    return markup3

def forums():
    markup3 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    back_to = types.KeyboardButton('<<<==')
    list1 = types.KeyboardButton('Список 1')
    list2 = types.KeyboardButton('Список 2')
    list3 = types.KeyboardButton('Список 3')
    markup3.add(list1, list2, list3, back_to)
    return markup3

def finances():
    markup3 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    back_to = types.KeyboardButton('<<==')
    mixer = types.KeyboardButton('Миксера')
    exchange = types.KeyboardButton('Обменники')
    wallet = types.KeyboardButton('Кошельки')
    markup3.add(mixer, exchange, wallet, back_to)
    return markup3

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    search_onion = types.KeyboardButton('Поиск')
    links_hosting = types.KeyboardButton('Хостинг')
    forum = types.KeyboardButton('Форум')
    info = types.KeyboardButton('ИНФО')
    finance = types.KeyboardButton('Финансы')
    go_to = types.KeyboardButton('Вперёд 👉')
    markup.add(info, search_onion, links_hosting, forum, finance, go_to)
    return markup

if __name__ == "__main__":
    bot.polling(none_stop=True)
