from vertex import Vertex

class Graph:
	def __init__(self):
		self.graph = dict()
		self.total_verts = 0 
		self.total_edges = 0
	

	def __contains__(self, v):
		return v in self.graph

	def __iter__(self):
		return iter(self.graph.values())


	def add_vertex(self, v):
		if type(v) != int: raise TypeError, 'vertex must be an integer'
		if v in self.graph:
			pass
		else:		
			n = Vertex(v)
			self.graph[v] = n
			self.total_verts += 1

	# assumes graph is directed and edges only go in one direction
	def add_edge(self, v1, v2, w=0):
		if v1 not in self.graph: nv = self.add_vertex(v1)
		if v2 not in self.graph: nv =  self.add_vertex(v2)
		self.graph[v1].add_neighbour(self.graph[v2], w)
		self.total_edges += 1


	def v1(self, v):
		"""gets one vertex from graph"""
		return self.graph[v]

	def vert_check(self, v):
		"""utility function for sys.args run.py"""
		if v in self.graph:
			return True
		else:
			return False

	def build_graph(self, lol):
		"""takes a list of lists and build a graph from each mini list"""
		for l in lol:
			if len(l) == 1: 
				self.add_vertex(l[0])
			if len(l) == 2:
				self.add_vertex(l[0])
				self.add_vertex(l[1])
			if len(l) == 3:
				self.add_edge(l[0], l[1], l[2])


	
	










