solved = [[0 for x in range(4)] for x in range(4)] 
for i in range(0, 4):
	for j in range(0, 4):
		solved[i][j] = j + 4*i + 1
solved[3][3] = -1

def printmatrix(tmp):
	for i in range(0, 4):
		print
		for j in range(0, 4):
			print str(tmp[i][j]) + ' ',


def getLoc(tmp, k): #gets the tuple which holds value k
	for i in range(0, 4):
		for j in range(0, 4):
			if tmp[i][j] == k:
				return (i, j) 

def mandist(tmp, num):
	x1 = getLoc(solved, num) 
	x2 = getLoc(tmp, num)
	ret = abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])
	print ret
	return ret


temp = [[0 for x in range(4)] for x in range(4)] 
for i in range(0, 4):
	for j in range(0, 4):
		temp[i][j] = i + 4*j + 1
temp[3][3] = -1


print 'SOLVED: ' 
printmatrix(solved)
print
print
print 'TEST PUZZLE:'
printmatrix(temp)
loc1 = getLoc(solved, 3)
loc2 = getLoc(temp, 3)
print
print loc1[0], loc1[1]
print loc2[0], loc2[1]
mandist(temp, 4)

