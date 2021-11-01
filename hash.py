# While Hash Tables tradition use key value pairs
# For this assignment you may assume the value may be hashed directly. 
# In practice, the only changes to support key/value pairs would be in __getKey()

# Be sure to implement rehashing

# Be sure to use some other data structure internally

class HashTable:

	# set up the hash table, with no values in it
	def __init__(self):
		pass
		
	# given some input, figure out its hash values
	# * You may use python hash() in this method
	def __getKey(self, x):
		pass
		
	# rehash the table if it is not of appropriate size
	# * Rehashing is required for this assignment, though this is private
	# * I reserve the write to change the parameters of random list generation in autograder to force rehashing
	def __rehash(self, m):
		pass
		
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
		pass
		
	# remove x from the hash table	
	def remove(self, x):
		pass
				
	# check if x is in the hash table
	def contains(self, x):
		pass
