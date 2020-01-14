#!/usr/bin/python3
#pip3 install python-telegram-bot requests
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import sanity_bot
from utils import trycatch
from datetime import datetime, timedelta


def store_clients():
    with open(CLIENTS_DATA, "w") as data_file:
        data_file.write('\n'.join(clients))
    print("Stored data:", clients)


def callback_alarm(context):
    context.bot.send_message(chat_id=context.job.context, text='Hi, This is a callback')


def schedule(context, client):
    context.bot.send_message(chat_id=client, text='A callback has been set!')
    context.job_queue.run_daily(callback_alarm, context=client, days=(0, 1, 2, 3, 4, 5, 6), time=datetime.now() + timedelta(seconds=5))


def subscribe(bot, context):
    client_id = str(bot.message.chat.id)
    if client_id not in clients:
        clients.append(client_id)
        store_clients()
        bot.message.reply_text(f"Hello! Your'e new here!")
        schedule(context, client_id)
    else:
        bot.message.reply_text(f"Welcome back =]")


def unsubscribe(bot, context):
    client_id = str(bot.message.chat.id)
    if client_id in clients:
        clients.remove(client_id)
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
