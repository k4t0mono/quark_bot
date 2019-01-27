import re
from enum import Enum

class CommandType(Enum):
	OTHER = 0
	LOG = 1
	ENTRY = 2


def parse(txt):
	words = txt.split()

	if words[0][0] == '.':
		return parse_command(words)
	else:
		return parse_entry(words)


def parse_command(words):
	if words[0].split('.')[1] == 'log':
		wallet = words[1] if len(words) > 1 else None
		return (CommandType.LOG, wallet)
	else:
		return parse_entry(words)


def parse_entry(words):
	if len(words) < 2:
		return (CommandType.OTHER, )

	words[0] = words[0].replace(',', '.')

	n = re.compile('\d*(\.\d{1,2})?')
	if n.match(words[0]):
		amout = float(words[0])
		desc = words[1]
		wallet = words[2] if len(words) > 2 else None

		return (CommandType.ENTRY, amout, desc, wallet)

	else:
		return (CommandType.OTHER, )

