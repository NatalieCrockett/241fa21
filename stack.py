# HW2: Stack

# Budget 10+ hours by Oct. 8 to complete this assignment if you received an autograder score of less than 50 on HW1.

# You may use code from class or prior assignments, but may not use internal Python data structures such as lists or arrays.
# You are strongly encouraged to use a Linked List. You can include a Linked List (sub)class inside this class, or use "import".

# Stacks implement a first-in-last-out storage. Only the most recently added (pushed) element may be seen (using peek) or removed (pop)
# This behavior is tested by the autograder.

# This assignment's solutions will not be covered in class, but will be eligible for resubmission.
# Instead this assignment is MANDATORY:
# I will require submission of a version of HW2 (or HW1) that receives a 100 from the autograder to submit your final grade.
# You may collaborate with classmates or use online resources, but please cite all sources of help after this comment:

class Stack:

	# an initializer to create a new stack object
	def __init__(self):
		pass
		
	# given some data, update the stack to include that data
	# input: data
	# output: nothing
	# side effect: data is now the first piece of data in the stack
	def push(self,data):
		pass
		
	# return the first piece of data without altering the stack
	# input: nothing
	# output: data
	# side effect: none
	def peek(self):
		pass
	
	# remove and return the first piece of data in the stack
	# input: nothing
	# output: data
	# side effect: data is no longer in stack
	def pop(self):
		pass
	
	# return True if there is no data in the stack
	def empty(self):
		pass
		
	# return the number of data objects currently in the stack
	def size(self):
		pass