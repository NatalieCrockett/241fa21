# Autograder

# This will attempt to perform intended tasks for HashTable. It will only use naturals, for simplicity.
# For each task, the autograder will:
#  - Define some expected behavior for some use case
#  - Perform the use case
#  - Award "points" if the result is as expected
#  - Either not award points (not too bad) or cause an error (pretty bad) if the result is not as expected
#    NOTE: Exception handling here could manage these errors, but it can be helpful to see them as well!

# This is a script to do the tests and print out what's happening
def singleTest(desc, target, val, pts):
	print("AUTOGRADER: " + desc)
	print(" - Expected Value: " + str(target))
	print(" - Observed Value: " + str(val))
	score = 0
	if (val == target):
		score = 20
		pts = pts + score
	print("POINTS: This section: " + str(score).zfill(2) + "/10 Total: " + str(pts).zfill(3) + "/100\n")	
	return pts

points = 0

print("\n --- AUTOGRADER: HashTable ---\n")
from hash import HashTable
t = HashTable()
# This generates a random list to be used
import random
l = list(set([random.randint(1,9999) for i in range(100)])) # use set() to remove duplicates

print("\nAUTOGRADER: Insert/Contains Testing: 60 pts\n")
points = singleTest("Checking empty contains nothing", True, all([not t.contains(x) for x in range(9999)]), points)
[t.insert(x) for x in l]
points = singleTest("Checking false contains after insert", True, all([not t.contains(x) or x in l for x in range(9999)]), points)
points = singleTest("Checking true contains after insert", True, all([t.contains(x) for x in l]), points)

print("\nAUTOGRADER: Remove/Contains Testing: 40 pts\n")
temp = l[:10] # get eleven elements (excpecting one duplicate)
l = l[10:] # get the remaining elements
[t.remove(x) for x in temp]
points = singleTest("Checking false contains after remove", True, all([not t.contains(x) or x in l for x in range(9999)]), points)
points = singleTest("Checking true contains after remove", True, all([t.contains(x) for x in l]), points)
	
