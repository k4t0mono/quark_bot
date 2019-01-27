import re
from enum import Enum

class CommandType(Enum):
	OTHER = 0
	LOG = 1
	ENTRY = 2


def parse(txt):
	if txt[0] == '.':
		return parse_command(txt)
	else:
		return parse_entry(txt)


def parse_command(txt):
	if txt.split('.')[1] == 'log':
		return CommandType.LOG
	else:
		return CommandType.OTHER


def parse_entry(txt):
	l = txt.split()
	l[0] = l[0].replace(',', '.')
	print(l)

	n = re.compile('\d*\.\d{0,2}')
	if n.match(l[0]):
		amout = float(l[0])
		desc = l[1]
		wallet = l[2] if len(l) > 2 else None

		return (CommandType.ENTRY, amout, desc, wallet)

	else:
		return CommandType.OTHER

