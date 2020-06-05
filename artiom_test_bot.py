import sys
import telebot
from langdetect import detect

TOKEN = sys.argv[1]

bot = telebot.TeleBot(TOKEN) 

@bot.message_handler(content_types=['text'])
def send_echo(message):

	lang = detect(message.text)

	prefix = "Really"
	suffix = "This is what you can say?"
	if lang == "he":
		prefix = "באמת"
		suffix = "זה מה שיש לך להגיד?"
	if lang == "ru" or lang == "mk":
		prefix = "Да ладно"
		suffix = "Это то что пришло тебе в голову?"

	bot.send_message(message.chat.id,  prefix + ", \"" + message.text + "!\" " + suffix)

bot.polling(none_stop = True)
