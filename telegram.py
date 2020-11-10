import telebot  # импортирую библиотеку
from config import keys, TOKEN
import time
from extensions import ConvertionException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)  # создаю класс бота


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    text = '''
    Чтобы начать работать введите команду боту в сдедующем формате: 
    \n<имя валюты>
    \n<в какую валюту перевести> 
    \n<кол-во переводимой валюты>
    '''
    bot.reply_to(message, f'Доброго времени суток! {message.chat.username}')
    time.sleep(1)
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for i in keys.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    if len(values) > 3:
        raise ConvertionException('Слишком много параметров')

    quote, base, amout = values
    total_base = CurrencyConverter.convert(quote, base, amout)
    text = f'Цена {amout} {quote}/{base}: {total_base}'

    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)  # стартую бот, none_stop=True позволяет работать даже если есть ошибки