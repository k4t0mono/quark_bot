import uuid


class Transaction:

	def __init__(self, amout, desc, wallet, duet):
		self.id = uuid.uuid4()
		self.amout = amout
		self.desc = desc
		self.wallet = wallet
		self.duet = duet

	def __str__(self):
		return '<Transaction amout={} desc={} wallet={} />'.format(
			self.amout, self.desc, self.wallet
		)

	def __repr__(self):
		return '{}({})'.format(self.__class__, self.__dict__)
