# -*- coding: utf-8 -*-

# 2016年9月28日21:45:16
# cloudIn 之
# matrix [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
def zhi(matrix):
	trMatrix = []
	for ele in zip(*matrix):
		trMatrix.append(ele)
	for j0 in range(len(matrix)):
		out = []
		for i0 in range(len(trMatrix))[::-1]:
			Head = matrix[j0][i0]
			print(Head)
			print('---------')
			for i1 in range(len(trMatrix))[::-1]:
				# i <-
				for j1 in range(len(matrix)):
				# j ->
					Tail = matrix[j1][i1]
			if Head != Tail:
				out.append(matrix)