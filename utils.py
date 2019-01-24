import logging


def get_logger(name, level=logging.INFO):
	logger = logging.getLogger(name)
	logging.basicConfig(
		level=level,
		format='[%(asctime)s] %(levelname)s - %(module)s.%(name)s - %(message)s'
	)
	return logger
