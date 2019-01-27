from utils import get_logger
from Transaction import Transaction


class Quark:

	def __init__(self, owner):
		self.owner = owner
		self.log = [] 
		self.balance = 0.0
		self.default_wallet = 0
		self.inspect()

	def add_transaction(self, amount, desc, **kwargs):
		wallet = self.get_wallet(kwargs)

		transaction = Transaction(amount, desc, wallet, -1)
		self.balance += amount

		get_logger('Quark.add_transaction').info(
			'new transaction {}'.format(transaction)
		)
		self.log.append(transaction)
		self.inspect()

		return self.balance

	def get_log(self, **kwargs):
		wallet = self.get_wallet(kwargs)

		log = [t for t in self.log if t.wallet == wallet]
		return log[-10:]


	def get_wallet(self, kwargs):
		if 'wallet' not in kwargs or not kwargs['wallet']:
			return self.default_wallet
		else:
			return kwargs['wallet']

	def inspect(self):
		print(str(self))

	def __str__(self):
		return '<Quark owner={} logs={} />'.format(self.owner, len(self.log))

	def __repr__(self):
		return '{}({})'.format(self.__class__, self.__dict__)
