import os
import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from utils import get_logger, restricted, log, log_command
from pprint import pprint
from random import choice
from Quark import Quark
from Parser import parse, CommandType


QUARK = Quark('k4t0mono')

@log
@restricted
def command_parse(bot, update):
	text = update.message.text
	ct = parse(text)
	print(ct)

	# if(text[0] == '.'):
		# (commad, *stuff) = text[1:].split()

		# if commad == 'log':
			# wallet = stuff[0] if len(stuff) else None
			# log = QUARK.get_log(wallet=wallet)
			# post_log(bot, update, log, wallet)

	# else:
		# (amout, desc) = text.split()
		# QUARK.add_transaction(amout, desc)
		# bot.send_message(
			# chat_id=update.message.chat_id,
			# text='Transaction added'
		# )


@log
def post_log(bot, update, log, wallet):
	bot.send_message(
		chat_id=update.message.chat_id,
		text='Transaction log from wallet {}'.format(wallet)
	)

	for t in log:
		a = 'Amout: *{}*'.format(t.amout)
		d = 'Desc: {}'.format(t.desc)

		bot.send_message(
			chat_id=update.message.chat_id,
			parse_mode='Markdown',
			text='{}\n{}'.format(a, d)
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

*.log <wallet>*
Get all transactions from the wallet

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
	dispatcher.add_handler(MessageHandler(Filters.text, command_parse))
	dispatcher.add_handler(MessageHandler(Filters.sticker , echo_sticker))

	get_logger(__name__).info('starting quark_bot')
	updater.start_polling()
