import re
from enum import Enum

class CommandType(Enum):
	OTHER = 0
	LOG = 1
	ENTRY = 2
	RECV = 3


def parse(txt):
	words = txt.split()

	if words[0][0] == '.':
		return parse_command(words)
	else:
		return parse_entry(words)


def parse_command(words):
	cmd = words[0][1:]

	if cmd == 'log':
		wallet = words[1] if len(words) > 1 else None
		return (CommandType.LOG, wallet)

	elif cmd == 'recieve' or cmd == 'recv':	
		amount = float(words[1])
		desc = words[2] if len(words) > 3 else 'Recived {:.2f}'.format(amount)
		wallet = words[3] if len(words) > 4 else None
		return (CommandType.ENTRY, amount, desc, wallet)

	else:
		return parse_entry(words)


def parse_entry(words):
	if len(words) < 2:
		return (CommandType.OTHER, )

	words[0] = words[0].replace(',', '.')

	n = re.compile('\d+(\.\d+)?|\.\d+')
	if n.match(words[0]):
		amout = float(words[0])
		desc = words[1]
		wallet = words[2] if len(words) > 2 else None

		return (CommandType.ENTRY, -amout, desc, wallet)

	else:
		return (CommandType.OTHER, )

