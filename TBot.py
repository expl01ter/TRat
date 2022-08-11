from pyfiglet import Figlet
from colorama import *
import time
import telebot
import os

os.system('clear')

f = Figlet(font='standard')

token='5592672952:AAH_wS4LS0D8vX3_Ep3ue_2M6aiktbtWjDI' # Токен Бота
bot = telebot.TeleBot(token)


print(" ")
print(Fore.BLUE + f.renderText('TBot') + Style.RESET_ALL)
print("TBot Лог Сервера: ")
print(" ")
print(" ")
print("==============================================")
print(" ")
print(" ")
print(" ")

@bot.message_handler(commands=['about'])
def about(message):
	print(Fore.BLUE + '/about' + Style.RESET_ALL + ' - Сообщение получено.')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Автор скрипта expl01ter. Этот бот сделан на лицензии GNU GPL V3, смотреть - /license')
	print(Fore.GREEN + 'Сообщение отправлено' + Style.RESET_ALL)
	
@bot.message_handler(commands=['start'])
def about(message):
	print(Fore.BLUE + '/start' + Style.RESET_ALL + ' - Сообщение получено.')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Открой меню чтобы узнать комнады')
	print(Fore.GREEN + 'Сообщение отправлено' + Style.RESET_ALL)

@bot.message_handler(commands=['site'])
def license(message):
	print(Fore.BLUE + '/site' + Style.RESET_ALL + ' - Сообщение получено.')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Сайт: expl01ter.github.io')
	print(Fore.GREEN + 'Сообщение отправлено' + Style.RESET_ALL)

@bot.message_handler(commands=['donate'])
def donate(message):
	print(Fore.BLUE + '/donate' + Style.RESET_ALL + ' - Сообщение получено.')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Купи мне чашку кофе: buymeacoffee.com/expl01ter')
	print(Fore.GREEN + 'Сообщение отправлено' + Fore.YELLOW + ' ВОЗМОЖНО ТЕБЕ КУПЯТ ЧАШКУ КОФФЕ!' + Style.RESET_ALL)

@bot.message_handler(commands=['repo'])
def repo(message):
	print(Fore.BLUE + '/donate' + Style.RESET_ALL + ' - Сообщение получено.')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Репозиторий https://github.com/expl01ter/TBot')
	print(Fore.GREEN + 'Сообщение отправлено' + Style.RESET_ALL)

@bot.message_handler(commands=['license'])
def repo(message):
	print(Fore.BLUE + '/license' + Style.RESET_ALL + ' - Сообщение получено.')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Лицензия: https://github.com/expl01ter/TBot/LICENSE')
	print(Fore.GREEN + 'Сообщение отправлено' + Style.RESET_ALL)

@bot.message_handler(commands=['help'])
def help(message):
	print(Fore.BLUE + '/help' + Style.RESET_ALL + ' - Сообщение получено.')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Просто открой меню.')
	print(Fore.GREEN + 'Сообщение отправлено' + Style.RESET_ALL)

bot.polling()