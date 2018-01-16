import sys

class Vertex:
	def __init__(self, key):
		self.key = key
		self.adj = dict()
		self.distance = sys.maxint
		self.pred = None
		self.visited = False

	def get_key(self):
		return self.key

	def get_pred(self):
		return self.pred

	def get_distance(self):
		return self.distance

	def get_neighbours(self):
		return self.adj

	def get_weight(self, n):
		if n in self.adj:
			return self.adj[n]
		else:
			raise KeyError, '{0} is not a neighbour of {1}'.format(n, self.key)

	def add_neighbour(self, n, weight=0):
		if n in self.adj:
			# print '{0} is alreay a neighbour of {1}, updating weight from {2} to {3}'.format(n, self.key, self.adj[n], weight)
			self.adj[n] = weight
		else:
			self.adj[n] = weight

	def set_distance(self, someint):
		if type(someint) != int: raise TypeError, 'distance must be an integer.'
		self.distance = someint

	def set_pred(self, p):
		if self.pred != p:
			self.pred = p
		else:
			print '{0} is already the predecessor to {1}'.format(p, self.key)

	def add_weight(self, n, w):
		if type(w) != int: raise TypeError, 'Weight must be an integer'

		if n in self.adj:
			self.adj[n] = w
		else:
			print '{0} is not a neighbour of {1}, adding {0}'.format(n, self.key)
			self.adj[n] = w

	def set_as_visited(self):
		self.visited = True
		return self.visited
