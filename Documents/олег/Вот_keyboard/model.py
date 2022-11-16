import sqlite3
from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, Filters
from telegram import Bot

def open(update, context):
    cursor = set_cursor(set_conn('data.db'))
    update.message.reply_text(show_all(cursor))

def start(update, context):
    return context.bot.send_message(update.effective_chat.id,
                                    'просмотреть справочник /open\n'
                                    + 'найти строку по фамилии /find\n'
                                    + 'добавить строку /addrow\n'
                                    + 'удалить строку /deleterow\n'
                                    + 'изменить данные в ячейке /change\n'
                                    + 'завершить текущую операцию /stop')


def stop(update, context):
    update.message.reply_text ("Введите /start")
    return ConversationHandler.END

def set_conn(file):
    conn = sqlite3.connect(file)
    return conn


def set_cursor(conn):
    cursor = conn.cursor()
    return cursor


def show_all(cursor):
    cursor.execute("select * from phone")
    results = str(f'(id,surname,name,phone, comment),{cursor.fetchall()}')
    return (results)


def show_row_surname(cursor, surname):
    cursor.execute(f"select * from phone where surname like '%{surname}%'")
    results = str(cursor.fetchall())
    return (results)


def add_row_sqlite(conn, cursor, lst):
    cursor.execute(
        f"insert into phone (surname ,name , phone, comment) "
        f"values ('{lst[0]}', '{lst[1]}', {lst[2]}, '{lst[3]}')")
    conn.commit()


def delete_row(conn, cursor, id):
    cursor.execute(
        f"delete from students where id={int(id)}"
    )
    conn.commit()


def update_row(conn, cursor, lst):
    cursor.execute(f"update students set {lst[1]}='{lst[2]}' where id={int(lst[0])}")
    conn.commit()
    conn.close()


def find_output(update, context):
    surname = update.message.text
    cursor = set_cursor(set_conn('data.db'))
    update.message.reply_text(show_row_surname(cursor, surname))


def add_row_output(update, context):
    lst = (update.message.text).split()
    conn = set_conn('data.db')
    cursor = set_cursor(conn)
    add_row_sqlite(conn, cursor, lst)


def deleterow_output(update, context):
    id = int(update.message.text)
    conn = set_conn('data.db')
    cursor = set_cursor(conn)
    delete_row(conn, cursor, id)


def change_output(update, context):
    lst = (update.message.text).split()
    conn = set_conn('data.db')
    cursor = set_cursor(conn)
    update_row(conn, cursor, lst)



def conv_handler(command, input, output):
    result = ConversationHandler(
        entry_points=[CommandHandler(command, input)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, output)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    return result