import logging
from functools import wraps


LIST_OF_ADMINS = [ 196044463 ]


def get_logger(name, level=logging.INFO):
	logger = logging.getLogger(name)
	logging.basicConfig(
		level=level,
		format='[%(asctime)s] %(levelname)s - %(name)s - %(message)s'
	)
	return logger


def log(func):
	@wraps(func)
	def wrapped(bot, update, *args, **kwargs):
		logger = get_logger(func.__name__)
		logger.info(
			'{} from {}({})'.format(
				func.__name__,
				update.message.from_user.username,
				update.message.from_user.id
			)
		)

		return func(bot, update, *args, **kwargs)

	return wrapped

def restricted(func):
	@wraps(func)
	def wrapped(bot, update, *args, **kwargs):
		logger = get_logger('restricted.{}'.format(func.__name__))
		user_id = update.effective_user.id

		if user_id not in LIST_OF_ADMINS:
			bot.send_message(chat_id=update.message.chat_id, text='Unauthorized access denied.')
			logger.warning(
				"Unauthorized access denied for {}({})".format(
					update.effective_user.username,
					update.effective_user.id
				)
			)
			return

		return func(bot, update, *args, **kwargs)

	return wrapped

def send_multiple_messages(bot, chat_id, msgs=[]):
	for msg in msgs:
		bot.send_message(
			chat_id=chat_id,
			parse_mode='Markdown',
			text=msg
		)
