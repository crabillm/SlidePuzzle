import copy
history = {}
size = 4
hole = (size - 1, size - 1)
myqueue = []

solved = [[0 for x in range(size)] for x in range(size)] 
for i in range(0, size):
	for j in range(0, size):
		solved[i][j] = j + size*i 

def m2s(tmp):
	ret = ''
	for i in range(0, size):
		for j in range(0, size):
			ret += (str(tmp[i][j]) + ' ')
	return ret


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
	if 0 <= hole[0] - 1:
		ret.append((hole[0] - 1, hole[1]))
	if size > hole[0] + 1:
		ret.append((hole[0] + 1, hole[1]))
	if 0 <= hole[1] - 1:
		ret.append((hole[0], hole[1] - 1))
	if  size > hole[1] + 1:
		ret.append((hole[0], hole[1] + 1))
	return ret


def getSwappedMatrix(tmp, swap):
	mycopy = copy.deepcopy(tmp)
	hole = findhole(mycopy)
	v = getVal(mycopy, swap)
#	print v, swap[0], swap[1]
	mycopy[hole[0]][hole[1]] = v
	mycopy[swap[0]][swap[1]] = 15
	#printmatrix(mycopy)
	return mycopy

#temp = [[0 for x in range(size)] for x in range(size)] 
#for i in range(0, size):
#	for j in range(0, size):
#		temp[i][j] = i + size*j
temp = copy.deepcopy(solved)
temp[0][0] = 4
temp[0][1] = 0
temp[0][2] = 1
temp[0][3] = 2
temp[1][0] = 8
temp[2][0] = 12
temp[3][0] = 15
temp[1][3] = 3
temp[2][3] = 7
temp[3][3] = 11


print 'SOLVED: ' 
printmatrix(solved)
print
print 'TEST PUZZLE:'
printmatrix(temp)
loc1 = getLoc(solved, 3)
loc2 = getLoc(temp, 3)
print
#print summandist(temp)
findhole(temp)
best = temp

for i in range(0, 10):
	mymin = 1000
	####################
	temp = copy.deepcopy(best)
	mylist = getAdjacencyList(temp)
	bestflip = (0, 0)
	for it in mylist:
		swapped = getSwappedMatrix(temp, it)
		attempt = summandist(swapped)
	#	print it[0], it[1], attempt
		if attempt < mymin:
			mymin = attempt
			best = swapped
			bestflip = it
	history[m2s(temp)] = m2s(best)
	myqueue.append(bestflip)
	if mymin == 0:
		print 'Found the Matrix!'
		printmatrix(best)
		break	
	#print '*****'
	#printmatrix(best)

m2s(best)
print
print 'swaps to reach solution:'
for x in myqueue:
	print x

for k in history:
	print k, history[k]



