import telebot


Token = '1473822720:AAEj6nJvTY0PY2Qpy1peXahsQAqN14sbtUo'
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, f'Доброго времени суток! {message.chat.username}')


bot.polling(none_stop=True)