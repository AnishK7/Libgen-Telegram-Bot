#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BookInfo import BookInfoProvider
from common import TELEGRAM_ACCESS_TOKEN, logging, logger, mode, HEROKU_APP_NAME
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os, sys



# Create the EventHandler and pass it your bot's token.
updater = Updater(token = TELEGRAM_ACCESS_TOKEN, use_context=True)

# Get the dispatcher to register handlers
dp = updater.dispatcher

if mode == "dev":
    def run(updater):
        updater.start_polling()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8440"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TELEGRAM_ACCESS_TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TELEGRAM_ACCESS_TOKEN))
else:
    logger.error("No MODE specified!")
    sys.exit(1)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update,context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Type your book title, I will try to find it.')


def help(update,context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update,context):
    print('Echo')
    provider = BookInfoProvider()
    books = provider.load_book_list(update.message.text, 'title')
    for book in books:
        update.message.reply_text(str(book))
        loc = 'book/' + book.title
        context.bot.send_document(chat_id=update.message.chat_id, document=open(loc, 'rb'),timeout = 120)
        os.remove(loc)

def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    # updater.start_polling()
    # updater.idle()

    run(updater)

if __name__ == '__main__':
    main()
