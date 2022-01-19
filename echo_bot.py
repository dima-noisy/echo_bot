import telebot

token = '2123133279:AAFzjGikj3s6foCLRh2XszGxrLmc43I9Pbw'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)