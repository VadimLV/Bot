import telebot, wikipedia, re
import random
from telebot import types


bot = telebot.TeleBot('5107342656:AAFp-hmBMaCWGvKkrUquFGza7rfeYOnAiIw')
wikipedia.set_lang("ru")

f = open('D:/temporary/TeleBot/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

a = open('D:/temporary/TeleBot/Quotes.txt', 'r', encoding='UTF-8')
Quotes = a.read().split('\n')
a.close()


@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Факты о Беларуси")
    item2 = types.KeyboardButton("Цитаты А.Г. Лукашенко")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Нажми кнопку: \nФакты о Беларуси или Цитаты А.Г. Лукашенко\n    Можно отправить мне любое слово, и я найду его значение на Wikipedia',
                     reply_markup=markup)


def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break

        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2

    except Exception as e:
        return 'В энциклопедии нет информации об этом'



@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Факты о Беларуси':
        answer = random.choice(facts)
        bot.send_message(message.chat.id, answer)
    elif message.text.strip() == 'Цитаты А.Г. Лукашенко':
        answer = random.choice(Quotes)
        bot.send_message(message.chat.id, answer)
    elif message.text.strip():
        boфt.send_message(message.chat.id, getwiki(message.text))




bot.polling(none_stop=True, interval=0)
