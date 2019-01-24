import os
import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from utils import get_logger
from pprint import pprint
from random import choice


def echo_text(bot, update):
	msg = update.message
	logger = logging.getLogger('echo_text')

	logger.info(
		'echo_text from {}({})'.format(
			msg.from_user.username,
			msg.from_user.id
		)
	)

	bot.send_message(
		chat_id=msg.chat_id,
		text=msg.text
	)


def echo_sticker(bot, update):
	msg = update.message
	logger = logging.getLogger('echo_sticker')

	logger.info(
		'echo_sticker from {}({})'.format(
			msg.from_user.username,
			msg.from_user.id
		)
	)

	ss = bot.get_sticker_set(msg.sticker.set_name)
	s = choice(ss.stickers)

	bot.send_sticker(
		chat_id=msg.chat_id,
		sticker=s
	)


if __name__ == '__main__':
	updater = Updater(token=os.environ['QUARK_TOKEN'])
	dispatcher = updater.dispatcher

	dispatcher.add_handler(MessageHandler(Filters.text, echo_text))
	dispatcher.add_handler(MessageHandler(Filters.sticker , echo_sticker))

	get_logger(__name__).info('starting quark_bot')
	updater.start_polling()
