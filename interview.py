# -*- coding: utf-8 -*-


# 1 2 3
# 4 5 6
# 7 8 9

# [0]3
# [1]2 6
# [2]1 5 9
# [3]4 8
# [4]7

def juzheng(n):
	middle = (2*n-1)/2
	for line in range(2*n-1):
		if line <= middle:
			# MAX = (line+1)*n
			print map(lambda x:x+1, [i for i in range((line+1)*n)[::-1]][::n+1])[:2*n-1-line][::-1]
		else:
			# MAX = n**2-(line-middle)
			print map(lambda x:x+1, [i for i in range(n**2-(line-middle))[::-1]][::n+1])[:2*n-1-line][::-1]
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
7 lines
# [0]4
# [1]3 8
# [2]2 7 12
# [3]1 6 11 16
# [4]5 10 15
# [5]9 14
# [6]13

		# 最大数 (line+1)*3
			print map(lambda x:x+1, [num[i] for i in range((line+1)*n)[::n+1]])
		# else:
		# # 最大数 (n**2)-(2*n-line)
		# 	print map(lambda x:num[x+1], [i for i in range((n**2)-(2*n-line))[::n+1]])