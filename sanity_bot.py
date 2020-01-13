import requests
import re
from utils import trycatch


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url


@trycatch
def bop(bot, context):
    url = get_url()
    print(f"Got {url}, sending reply")
    bot.message.reply_photo(url)


def echo(bot, context):
    print("Got echo, replying...")
    bot.message.reply_text("Sup")
