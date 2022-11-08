import telebot

from telebot import types

bot = telebot.TeleBot('5427079918:AAHJygnBqnwcNNJQkO3xw_U3zhbHIFWJyX4')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Barev, <b><u>{message.from_user.first_name} {message.from_user.last_name}</u></b> jan'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'qezel Hello ap jan', parse_mode='html')
        # bot.send_message(message.chat.id, message, parse_mode='html') ---sax infon beruma
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'qo id kodne: {message.from_user.id}', parse_mode='html')
    elif message.text == 'photo':
        photo = open('amis amsativ-removebg-preview.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'es qez chaskaca', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'nkare vate chi!!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('mtnel siti mej', url='https://instagram.com'))
    bot.send_message(message.chat.id, 'mti instagram!!', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'mti instagram!!', reply_markup=markup)


bot.polling(none_stop=True)
#bot.infinity_polling()