import time

import telegram
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    ConversationHandler, MessageHandler, filters
)

import config
import message_texts

QUESTIONS, TZ_INFO, SETUP_END = range(3)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.from_user.id)
    await update.message.reply_text(message_texts.START_TEXT)


async def get_questions_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(message_texts.QUESTIONS)
    # await context.user_data.
    return TZ_INFO


async def get_tz_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[telegram.KeyboardButton(text='Прислать геопозицию', request_location=True)]]

    # db.write()

    await update.message.reply_text(message_texts.TZ_INFO, reply_markup=ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    ))
    return SETUP_END


async def setup_end(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message)
    print(update.message.location)
    await update.message.reply_text(message_texts.SUCCESS, reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(message_texts.CANCELLATION)
    return ConversationHandler.END

if __name__ == '__main__':
    application = ApplicationBuilder().token(config.TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("setup", get_questions_info)],
        states={
            TZ_INFO: [MessageHandler(filters.ALL, get_tz_info)],
            SETUP_END: [MessageHandler(filters.ALL, setup_end)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    application.add_handler(conversation_handler)

    application.run_polling()
