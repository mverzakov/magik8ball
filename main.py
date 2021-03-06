#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.

"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from weather import get_weather
from img_gen import generate_img
import logging
import os.path
import time

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Write a question - get an answer.')


def echo(bot, update):
    message = update.message.text.lower()
    if message.find(u'погода') != -1 or message.find(u'температура') != -1:
        weather = get_weather()
        # generate_img('{}'.format(weather['temp']), weather['description'], update.message.chat_id)
        # file_name = 'answers/weather-{}.png'.format(update.message.chat_id)
        # path = os.path.join(os.path.dirname(os.path.dirname(__file__)), file_name)
        # img_file = open(file_name, 'rb')
        bot.sendMessage(update.message.chat_id, text=u'Сейчас {}, {}°'.format(weather['description'], weather['temp']))
    elif message.startswith(u'можно'):
        img_file = open('answers/answer{}.png'.format(random.randint(1, 21)), 'rb')
        bot.sendPhoto(update.message.chat_id, photo=img_file)
    else:
        img_file = open('answers/answer{}.png'.format(random.randint(1, 20)), 'rb')
        bot.sendPhoto(update.message.chat_id, photo=img_file)



def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("233760382:AAFaCGOpU6elGE-_wqErpzJlWSDitK75HkI")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler([Filters.text], echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()