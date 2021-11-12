# While Hash Tables tradition use key value pairs
# For this assignment you may assume the value may be hashed directly. 
# In practice, the only changes to support key/value pairs would be in __getKey()

# Be sure to implement rehashing

# Be sure to use some other data structure internally

class HashTable:

	# set up the hash table, with no values in it
	def __init__(self):
		self.most = 4
		self.size = 0
		self.table = [None] * self.most
		
	# given some input, figure out its hash values
	# * You may use python hash() in this method
	def __getKey(self, x):
		return hash(x) / self.most
		
	# rehash the table if it is not of appropriate size
	# * Rehashing is required for this assignment, though this is private
	# * I reserve the right to change the parameters of random list generation in autograder to force rehashing
	def __rehash(self, m):
		if m <= 4:
			return self
		self.most = m
		prev = self.table
		for i in prev:
			if i != None:
				self.insert(i)
		return
		
	# insert x into the hash table
	# * Use some data structure to deal with collisions, such as:
	#   - Python List
	#   - Linked List
	#   - BST
	#   - Python Set
	#   - Python Dictionary
	#   - Stack
	#   - Queue
	def insert(self, x):
		self.size = self.size + 1
		if self.size > self.most//2:
			self.__rehash(self.most * 2)
		p = self.__getKey(x)
		while self.table[p] != None:
			p = (p + 1) / self.most
		self.table[p] = x
		return
		
	# remove x from the hash table	
	def remove(self, x):
		self.size = self.size - 1
		p = self.__getKey(x)
		while self.table[p] != None:
			p = (p + 1) / self.most
		new = (p + 1) / self.most
		while self.table[new] != None:
			if self.__getKey(self.table[new]) > p:
				new = (new + 1) / self.most
			else:
				p = new
				new = (p + 1) / self.most
		self.table[p] = None
		if self.size < self.most // 4:
			self.__rehash(self.most //2)
		return
		
				
	# check if x is in the hash table
	def contains(self, x):
		p = self.__getKey(x)
		while self.table[p] != None:
			if self.table[p] == x:
				return True
		return False
