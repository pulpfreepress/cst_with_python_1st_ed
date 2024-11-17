"""Implement the definition of a Payable entitiy."""

from abc import ABC, abstractmethod

class Payable(ABC):
	"""Provides specification for pay() method."""

	@abstractmethod
	def pay(self)->float:
		pass

