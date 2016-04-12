def grid():
	txt = open("result.txt")
	words = txt.read()
	lst = words.split("\n")
	answer = [[0 for _ in range(9)] for _ in range(9)]
	for item in lst:
		if "TRUE" in item:
			x, y, z = int(item[9]) - 1, int(item[10]) - 1, int(item[11])
			if answer[x][y] != 0:
				print "ERROR SOMETHIGN WRONG"
			else:
				answer[x][y] = z
	for line in answer:
		print line

grid()