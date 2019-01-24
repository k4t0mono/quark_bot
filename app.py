import os
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler


def echo(bot, update):
	print('echo from {}'.format(update.message.from_user.username))

	bot.send_message(
		chat_id=update.message.chat_id,
		text=update.message.text
	)


if __name__ == '__main__':
	updater = Updater(token=os.environ['QUARK_TOKEN'])
	dispatcher = updater.dispatcher

	dispatcher.add_handler(MessageHandler(Filters.text, echo))

	updater.start_polling()
	print('starting bot...')
