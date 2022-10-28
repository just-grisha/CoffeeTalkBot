import telebot

TOKEN = '5742628016:AAGf8TffSFrJQGlJKMPjDF0gNEDADPUatJY'

bot = telebot.TeleBot(TOKEN)

'''
@bot.message_handler(commands=['start'])
def start(message):
    mes = f"Привет, {message.from_user.fisrt_name} {message.from_user.last_name}"
    bot.send_message(message.chat.id, mes, parse_mode=None)


@bot.message_handler()
def say_hello_to_user(message):
    if message.text == "Lol":
        bot.send_message(message.chat.id, f"Привет,{message.first_name}", parse_mode=None)

'''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


bot.polling()
while True:
