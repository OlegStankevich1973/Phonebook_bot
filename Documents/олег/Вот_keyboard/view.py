def find(update, context):
    update.message.reply_text("Введите фамилию для поиска")
    return 1


def add_row(update, context):
    update.message.reply_text("Введите фамилию, имя, телефон и комментарий через пробел")
    return 1


def deleterow(update, context):
    update.message.reply_text("Введите индекс для удаления")
    return 1


def change_cell(update, context):
    update.message.reply_text("Введите индекс, колонку и новое значение через пробел")
    return 1