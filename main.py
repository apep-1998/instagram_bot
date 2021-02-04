from tools import config
import settings
import time
# start telegram bot import
from telepot.loop import MessageLoop
import telepot
# end telegram bot import


if config.get_key("users", "main_config.json") == None:
    config.set_key("users", [], "main_config.json")

users = config.get_key("users", "main_config.json")


bot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)

def chat_message_handel(message):
    pass

def button_message_handel(message):
    pass

MessageLoop(bot,{'chat': chat_message_handel,
                 'callback_query': button_message_handel}).run_as_thread()



while True:
    for user in users:
        user.start()

    time.sleep(10)