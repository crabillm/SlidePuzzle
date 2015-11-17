import copy
size = 4
hole = (size - 1, size - 1)

solved = [[0 for x in range(size)] for x in range(size)] 
for i in range(0, size):
	for j in range(0, size):
		solved[i][j] = j + size*i 

def printmatrix(tmp):
	for i in range(0, size):
		print
		for j in range(0, size):
			print str(tmp[i][j]) + ' ',
	print			


def getLoc(tmp, k): #gets the tuple which holds value k
	for i in range(0, size):
		for j in range(0, size):
			if tmp[i][j] == k:
				return (i, j) 

def getVal(tmp, k):
	return tmp[k[0]][k[1]]


def mandist(tmp, num):
	x2 = getLoc(tmp, num)
	ret = abs(num/4 - x2[0]) + abs(num % 4 - x2[1])
	return ret


def summandist(tmp):
	count = 0
	for i in range(0, size * size):
		count += mandist(tmp, i)
	return count
		
def findhole(tmp):
	for i in range(0, size):
		for j in range(0, size):
			if tmp[i][j] == 15:
		#		print 'hole at ' + str(i) + ' ' + str(j)
				return (i, j)

def getAdjacencyList(tmp):
	ret = []
	hole = findhole(tmp) 
#	print hole[0], hole[1]
	if 0 <= hole[0] - 1:
		ret.append((hole[0] - 1, hole[1]))
	if size > hole[0] + 1:
		ret.append((hole[0] + 1, hole[1]))
	if 0 <= hole[1] - 1:
		ret.append((hole[0], hole[1] - 1))
	if  size > hole[1] + 1:
		ret.append((hole[0], hole[1] + 1))
#	print 'ret is ' + str(len(ret)) + ' long'
#	for x in ret:
#		print x[0], x[1]
	return ret


def getSwappedMatrix(tmp, swap):
	mycopy = copy.deepcopy(tmp)
	hole = findhole(mycopy)
	v = getVal(mycopy, swap)
#	print v, swap[0], swap[1]
	mycopy[hole[0]][hole[1]] = v
	mycopy[swap[0]][swap[1]] = 15
	printmatrix(mycopy)
	return mycopy


temp = [[0 for x in range(size)] for x in range(size)] 
for i in range(0, size):
	for j in range(0, size):
		temp[i][j] = i + size*j
temp[2][2] = 15
temp[size - 1][size - 1] = 10

print 'SOLVED: ' 
printmatrix(solved)
print
print 'TEST PUZZLE:'
printmatrix(temp)
loc1 = getLoc(solved, 3)
loc2 = getLoc(temp, 3)
print
#print loc1[0], loc1[1]
#print loc2[0], loc2[1]
print summandist(temp)
findhole(temp)
mylist = getAdjacencyList(temp)
mymin = 1000 
best = temp
for it in mylist:
	swapped = getSwappedMatrix(temp, it)
	attempt = summandist(swapped)
	print it[0], it[1], attempt
	if attempt < mymin:
		mymin = attempt
		best = swapped
print '*****'
printmatrix(best)

for i in range(0, 12):
	mymin = 1000
	####################
	temp = copy.deepcopy(best)
	mylist = getAdjacencyList(temp)
	for it in mylist:
		swapped = getSwappedMatrix(temp, it)
		attempt = summandist(swapped)
		print it[0], it[1], attempt
		if attempt <= mymin:
			mymin = attempt
			best = swapped
	print '*****'
	printmatrix(best)





