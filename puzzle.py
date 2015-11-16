def printmatrix(tmp):
	for i in range(0, 4):
		print
		for j in range(0, 4):
			print str(tmp[i][j]) + ' ',




solved = [[0 for x in range(4)] for x in range(4)] 
for i in range(0, 4):
	for j in range(0, 4):
		solved[i][j] = j + 4*i + 1
solved[3][3] = -1

printmatrix(solved)
