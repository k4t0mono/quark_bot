import os
import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from utils import get_logger, restricted, log
from pprint import pprint
from random import choice

@log
def echo_text(bot, update):
	msg = update.message

	bot.send_message(
		chat_id=msg.chat_id,
		text=msg.text
	)


@log
def echo_sticker(bot, update):
	msg = update.message
	ss = bot.get_sticker_set(msg.sticker.set_name)
	s = choice(ss.stickers)

	bot.send_sticker(
		chat_id=msg.chat_id,
		sticker=s
	)


@log
@restricted
def get_help(bot, update):
	msg = update.message

	txt = """
Commands:

*/new_wallet <name> [balance]*
Add a new wallet to the list

*/list_wallets*
List the avaliable wallets

*/set_default <name>*
Set the default wallet for transactions

*/get_default*
Get the default wallet

*/log*
Get all transactions

To add a new transaction just add send a message on the format:
<desc> <value> [wallet]
"""

	bot.send_message(
		chat_id=msg.chat_id,
		parse_mode='Markdown',
		text=txt
	)


if __name__ == '__main__':
	updater = Updater(token=os.environ['QUARK_TOKEN'])
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('help', get_help))
	dispatcher.add_handler(MessageHandler(Filters.text, echo_text))
	dispatcher.add_handler(MessageHandler(Filters.sticker , echo_sticker))

	get_logger(__name__).info('starting quark_bot')
	updater.start_polling()
