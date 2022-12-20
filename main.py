import telebot
import random
import requests
from telebot import types
from bs4 import BeautifulSoup as b
url = 'https://www.anekdot.ru/release/anekdot/week/'

token = '5874861196:AAGN4LY7HNcWJaijhYZuLAZmZ9VTf4jv49s'

def parser (url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]
list_of_jobs = parser(url)
random.shuffle(list_of_jobs)
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Анекдот")
        item2=types.KeyboardButton("Словарь")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \nАнекдот \nСловарь ',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Анекдот' :
            answer = list_of_jobs[0]
    
    elif message.text.strip() == 'Словарь':
            answer = 'Словарь'
    
    bot.send_message(message.chat.id, answer)
    del list_of_jobs[0]






bot.infinity_polling()




