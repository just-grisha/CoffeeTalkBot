from aiogram import Bot, Dispatcher, executor, types
import time
import logging
import telebot
import sqlite3
import SerchAlg

TOKEN = "5742628016:AAGf8TffSFrJQGlJKMPjDF0gNEDADPUatJY"



db = sqlite3.connect("UsersData.db")

c = db.cursor()


first_name = ''
last_name = ''
age = ''
company = ''
interests = ''

def Bot_():
    bot = telebot.TeleBot(TOKEN)
    @bot.message_handler(commands=['help'])
    def _command_(message):
        bot.send_message(message.chat.id,"Список команд \n /start - создания профиля \n /edit - извменение профиля /find - найти собеседника ")
        bot.register_next_step_handler(message, _command_)
    @bot.message_handler(commands=['edit'])
    def _command_(message):
        bot.send_message(message.chat.id, "Пока что тут пусто")  # тут нужно сделать кнопку в будущем
        bot.register_next_step_handler(message, get_name)



    @bot.message_handler(commands=['find'])
    def go_to_find(message):
        bot.send_message(message.chat.id, "Поехали искать")
        bot.register_next_step_handler(message, find_users)


    @bot.message_handler(commands=['start'])
    def _command_(message):
        bot.send_message(message.chat.id, "Введите имя: ")
        bot.register_next_step_handler(message, get_name)


    def find_users():
        # встроить алгоритм поиска из main3 SearchAlg.find()
        pass


    def get_name(message):
        global first_name
        firist_name = message.text  # добавление в бд
        # bot.send_message(message.chat.id,message.text)
        bot.send_message(message.chat.id, "Введите фамилию: ")
        bot.register_next_step_handler(message, get_last_name)


    def get_last_name(message):
        global last_name
        last_name = message.text
        # bot.send_message(message.chat.id, message.text)
        bot.send_message(message.chat.id, "Введите возраст: ")
        bot.register_next_step_handler(message, get_age)


    def get_age(message):
        global age
        age = message.text
        # bot.send_message(message.chat.id, message.text)
        bot.send_message(message.chat.id, "Введите компанию в которой вы работаете: ")
        bot.register_next_step_handler(message, get_company)


    def get_company(message):
        global company
        company = message.text
        # проверка из бд компании
        # bot.send_message(message.chat.id, message.text)
        bot.send_message(message.chat.id, "Введите интересы в формате слово пробел \n Например, книги спорт фильмы")
        bot.register_next_step_handler(message, get_interests)


    def get_interests(message):
        interests = []  # message.text надо запихунть сюда и в бд добавить
        bot.send_message(message.chat.id, "Ваши данные записаны")
        bot.register_next_step_handler(message, load_to_bd)


    def load_to_bd(message):
        global first_name, last_name, age, company  # + interests надо добавить main.py 70 -82
        c.execute(f"INSERT INTO user(first_name,last_name,age,company) VALUES(?,?,?,?)",(first_name, last_name, age, company))


    db.commit()
    db.close()
    bot.infinity_polling()
Bot_()
'''
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f"{user_id} {user_full_name} {time.asctime()}")
    await message.reply(f"Hi ,{user_full_name} Готов начать заполнение профиля?")

@dp.message_handler()
async def get_inf(message: types.Message):
    if message.text == "Да" or message.text == "да":
        await bot.send_message(message.from_user.id,"Как тебе зовут?")
        first_name = message.text
        bot.register_next_stpe
    await message.reply(message.from_user.id, first_name)
    #await bot.send_message(message.from_user.id,message.text)



if __name__ == "__main__":
    executor.start_polling(dp)
'''
