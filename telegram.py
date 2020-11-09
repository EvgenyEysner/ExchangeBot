import telebot


Token = ''
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, f'Доброго времени суток! {message.chat.username}')


bot.polling(none_stop=True)
