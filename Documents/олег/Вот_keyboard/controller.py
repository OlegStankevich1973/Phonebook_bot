import model, view
from telegram import Bot
from telegram.ext import Updater, CommandHandler


def run():
    bot_token = "5648685451:AAHmXJ365bBNWrQWq0XdNqHHOQTw7O6K0UU"
    bot = Bot(bot_token)
    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', model.start)
    open_handler = CommandHandler('open', model.open)
    find_handler = model.conv_handler('find', view.find, model.find_output)
    add_row_handler = model.conv_handler('addrow', view.add_row, model.add_row_output)
    delete_handler = model.conv_handler('deleterow', view.deleterow, model.deleterow_output)
    change_handler = model.conv_handler('change', view.change_cell, model.change_output)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(open_handler)
    dispatcher.add_handler(find_handler)
    dispatcher.add_handler(add_row_handler)
    dispatcher.add_handler(delete_handler)
    dispatcher.add_handler(change_handler)

    updater.start_polling()
    updater.idle()
