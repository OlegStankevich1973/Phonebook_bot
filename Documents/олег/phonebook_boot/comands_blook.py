
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from telegram import Update, Bot
import sqlite3

def start(update, context):
    context.bot.send_message(update.effective_chat.id,
        f"Привет! Это телефонный справочник!\n"
        f"Выберите необходимое действие:\n"
        f"показать все /show \n"
        f"показать конкретного человека /show_person\n"
        f"удалить запись /del_note\n"
        f"добавить запись /add_note\n"
    )


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END
def show(update, context):
    # подгружаем базу
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("select * from phone")  # select * - выбрать все
    results = cursor.fetchall()
    context.bot.send_message(update.effective_chat.id,f"{results}")  # выводим в бот

    # Запрашиваем информацию

def show_person(update, context):
    context.bot.send_message(update.effective_chat.id,f"Введите фамилию: \n Для выхода напишите /stop")
    return 1

    # Обрабатываем запрос

def show_person_out(update, context):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    text = update.message.text  # считали из бота
    cursor.execute(f"select * from phone where surname like '%{text}%'")
    results = cursor.fetchall()
    update.message.reply_text(f"{results}")
   

def del_note(update, context):
    context.bot.send_message(update.effective_chat.id, f"Введите индекс для удаления: \n Для выхода напишите /stop")
    return 1

# Обрабатываем запрос


def del_note_out(update, context):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    text = update.message.text   # считали из бота
    cursor.execute(f"delete from phone where id={text}")
    conn.commit()
    update.message.reply_text(f"информация удалена")


def add_note(update, context):
        context.bot.send_message(
            update.effective_chat.id, f"Введите данные для добавления: \n Для выхода напишите /stop")
        return 1

    # Обрабатываем запрос

def add_note_out(update, context):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    text = update.message.text  # считали из бота
    text = text.split()  # разделили строки по пробелу на список строк
    cursor.execute(f"insert into phone (id,surname, name,phone, description)"f"values ('{text[0]}', '{text[1]}', '{text[2]}', '{text[3]}','{text[4]}' )")
    conn.commit()
    update.message.reply_text(f"информация добавлена")
