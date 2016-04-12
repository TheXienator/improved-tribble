def sudokuSTP(starting):
	nums = "123456789"
	for i in nums:
		for j in nums:
			lst = []
			for k in nums:
				lst.append("v" + i+j+k)
			print ', '.join(lst) + " : BOOLEAN;" 
	for num in starting:
		print "ASSERT(v" + num + ");"

	def section(i, j, k):
		i, j = int(i), int(j)
		lst = []
		for a in range(3):
			for b in range(3):
				x = a + ((i-1) / 3) * 3 + 1
				y = b + ((j-1) / 3) * 3 + 1
				if x != i or y != j:
					lst.append("NOT(v" + str(x)+str(y)+k + ")")
		return lst

	for i in nums:
		for j in nums:
			for k in nums:
				# can only have one number per box
				lst = ["NOT(v" + i+j+a +")" for a in nums if a != k]
				print "ASSERT(v" + i+j+k + " <=> (" + ' AND '.join(lst) + "));"
				# can only have one number per section
				lst = section(i, j, k)
				print "ASSERT(v" + i+j+k + " <=> (" + ' AND '.join(lst) + "));"
				# can only have one number per row
				lst = ["NOT(v" + a+j+k +")" for a in nums if a != i]
				print "ASSERT(v" + i+j+k + " <=> (" + ' AND '.join(lst) + "));"
				# can only have one number per col
				lst = ["NOT(v" + i+a+k +")" for a in nums if a != j]
				print "ASSERT(v" + i+j+k + " <=> (" + ' AND '.join(lst) + "));"

vals = ["331", "623", "532", "828", "925", "445", "647", "354", "751", "269", "715", "877", "973", "382", "581", "594", "999"]
sudokuSTP(vals)
