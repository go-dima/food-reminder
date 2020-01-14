#!/usr/bin/python3
#pip3 install python-telegram-bot requests
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import sanity_bot
from utils import trycatch


def store_clients():
    print("Storing data")
    with open(CLIENTS_DATA, "w") as data_file:
        data_file.write('\n'.join(clients))


def subscribe(bot, context):
    client = str(bot.message.chat.id)
    print(client)
    if client not in clients:
        clients.append(client)
        store_clients()
        bot.message.reply_text(f"Hello! Your'e new here!")
    else:
        bot.message.reply_text(f"Welcome back =]")


def unsubscribe(bot, context):
    client = str(bot.message.chat.id)
    print(client)
    if client in clients:
        clients.remove(client)
        store_clients()
        bot.message.reply_text(f"Goodbye!")
    else:
        bot.message.reply_text(f"Please subscribe first!")


CLIENTS_DATA = "clients-list.dat"
YOUR_TOKEN = open("bot.token", "r").read().splitlines()[0]
clients = open(CLIENTS_DATA, "r").read().splitlines()


def main():
    updater = Updater(YOUR_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('echo', sanity_bot.echo))
    dp.add_handler(CommandHandler('sub', subscribe))
    dp.add_handler(CommandHandler('unsub', unsubscribe))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
