class MinHeap:

	def __init__(self):
		self.heap = []
		self.pos = {} # holds vert as k and index position in heap as val, starting from 0
		self.currentsize = 0 

	def is_empty(self):
		if self.currentsize > 0:
			return False
		else:
			return True

	def get_head(self):
		"""Peeks at the current smallest item in the heap"""
		return self.heap[0]

	def get_heap_value(self, i):
		"""Returns the value of a particular index in the heap"""
		if i < self.currentsize:
			return self.heap[i]
		else:
			raise IndexError, 'Item does not exists in list'

	def get_heap(self):
		return self.heap

	def heap_size(self):
		return self.currentsize


	def get_parent_index(self, childindex):
		"""Works out the parent index of a childindex using the heap property; 
		((childindex - 1)/2) floored which will return the index of the childs parent"""
		return (childindex-1)//2

		
	def has_parent(self, index):
		"""Checks to see if a childindex has a parent. This is a useful function to break
		out of loops with. """
		return self.get_parent_index(index) >= 0

	
	def get_parent(self, child):
		"""if not the root node get the actual value at the parentindex"""
		if child == 0:
			None
		else:
			return self.heap[self.get_parent_index(child)]


	def add(self, dist, key):
		"""add new item and then bubble it up"""
		newval = [dist, key]
		self.pos[key] = None
		self.heap.append(newval)
		self.currentsize += 1
		self._heapifyup()
		

	def del_min(self):
		"""deletes the minimum node (root), makes the last node root and bubbles it down 
		if its out of place""" 
		if self.is_empty() == True:
			return None

		root = self.heap[0]
		self.heap[0] = self.heap[-1]
		self.heap.pop()
		del self.pos[root[1]]
		self.currentsize -= 1
		self.min_heapify(0)
		return root 

	def min_heapify(self, index):
		"""takes an element from the heap and bubbles it down till its in the correct position"""
		s = index
		left =  (2*index) + 1 # left child index 
		right = (2*index) + 2 # right child index

		if left < self.currentsize and self.heap[left][0] < self.heap[s][0]:
			s = left
		if right < self.currentsize and self.heap[right][0] < self.heap[s][0]:
			s = right
		if s != index:
			self.swap_dict(self.heap[s], s, self.heap[index], index)
			self.swap(s, index)
			self.min_heapify(s)

	def _heapifyup(self):
		"""takes the last element of the heap and bubbles it up till its in the correct position"""
		i = self.currentsize - 1
		if i < 1:
			pass
		while self.has_parent(i) == True:
			x = self.get_parent(i) 
			if x[0] > self.heap[i][0]:
				self.swap_dict(self.get_parent(i), self.get_parent_index(i), self.heap[i], i)
				self.swap(self.get_parent_index(i), i)
			i = self.get_parent_index(i)
		#set's postion of last key in the dict that will not get swapped	
		self.pos[self.heap[self.currentsize-1][1]] = self.currentsize-1

	def swap_dict(self, a, aindex, b, bindex):
		"""utility function for swapping two values in dict"""
		temp = a[1]
		temp2 = b[1]
		self.pos[temp] = bindex
		self.pos[temp2] = aindex


	def swap(self, a, b):
		"""utility function for swapping two values in heap"""
		temp = self.heap[a]
		self.heap[a] = self.heap[b]
		self.heap[b] = temp


	def decrease_val(self, v, newdist):
		"""looks up the vertex index in dict and changes vertex distance then re-heapifies"""
		i = self.pos[v]
		self.heap[i][0] = newdist 
		while self.has_parent(i) == True:
			if self.heap[i][0] < self.heap[self.get_parent_index(i)][0]:
				self.swap_dict(self.get_parent(i), self.get_parent_index(i), self.heap[i], i)
				self.swap(self.get_parent_index(i), i)

			i = self.get_parent_index(i)



	def build_heap(self, alist):
		"""not a great way to do it but will work for now"""
		for c in alist:
			self.add(c[0], c[1])

		return self.heap

