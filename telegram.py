import telebot  # импортирую библиотеку
from config import keys, TOKEN
import time
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)  # создаю класс бота


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    text = '''
    Чтобы начать работать введите команду боту в сдедующем формате через пробел: 
    \n имя валюты
    \n в какую валюту перевести
    \n кол-во переводимой валюты
    \n вывести информацию о доступных валютах можно командой /values
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
    try:
        msg_values = message.text.upper().split(' ')
        if len(msg_values) != 3:
            raise APIException('Слишком много параметров')

        quote, base, amout = msg_values
        total_base = round(CurrencyConverter.get_price(quote, base, amout), 2)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amout} {quote}/{base}: {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)  # стартую бот, none_stop=True позволяет работать даже если есть ошибки