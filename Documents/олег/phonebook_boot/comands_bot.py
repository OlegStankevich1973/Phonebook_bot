
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from telegram import Update, Bot
# import sqlite3  # иморт sqlite3
from comands_blook import*
import sqlite3

bot_token = '5648685451:AAHmXJ365bBNWrQWq0XdNqHHOQTw7O6K0UU'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


show_person_handler = ConversationHandler(
    # входная точка
    # попадаем сюда при вводе в боте /show_person
    entry_points=[CommandHandler('show_person', show_person)],

    # Состояние внутри диалога.
    states={
        # обработка запроса в функции show_person_out
        1: [MessageHandler(Filters.text & ~Filters.command, show_person_out)],
    },

    # Точка прерывания диалога. В данном случае — команда /stop.
    fallbacks=[CommandHandler('stop', stop)]
)


del_note_handler = ConversationHandler(
    # входная точка
    # попадаем сюда при вводе в боте /del_note
    entry_points=[CommandHandler('del_note', del_note)],

    # Состояние внутри диалога.
    states={
        # обработка запроса в функции del_note_out
        1: [MessageHandler(Filters.text & ~Filters.command, del_note_out)],
    },

    # Точка прерывания диалога. В данном случае — команда /stop.
    fallbacks=[CommandHandler('stop', stop)]
)



# объединяем запрос информации и обработку информации в один диалог
add_note_handler = ConversationHandler(
    # попадаем сюда при вводе в боте /add_note
    entry_points=[CommandHandler('add_note', add_note)],

    # Состояние внутри диалога.
    states={
        # обработка запроса в функции add_note_out
        1: [MessageHandler(Filters.text & ~Filters.command, add_note_out)],
    },

    # Точка прерывания диалога. В данном случае — команда /stop.
    fallbacks=[CommandHandler('stop', stop)]
)


'Регистрируем все обработчики и передаем их в диспетчер'

start_handler = CommandHandler('start', start)  # стартовое меню
show_handler = CommandHandler('show', show)    # показ всей книги


dispatcher.add_handler(start_handler)  # стартовое меню
dispatcher.add_handler(show_handler)    # показ всей книги
dispatcher.add_handler(show_person_handler)    # показ конкретного человека
dispatcher.add_handler(del_note_handler)    # удаление записи
dispatcher.add_handler(add_note_handler)    # добавление записи


updater.start_polling()
updater.idle()
