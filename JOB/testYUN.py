# _*_coding:utf-8_*_

# 1
from collection import Counter

List = ['abc','abc','abc','dec','dec','dec','trre','trre','ddd','ddd']
# 1.1
Count = Counter(List)
# 1.2
List.sort(key=lambda x: x[2])
NewList = sorted(List, key=lambda x: x[2])

# 2
import itertools
List = ['a', 'b', 'c']
iters = itertools.permutations(List, 3)
for i in iters:
	print(''.join([ele for ele in i]))

List = ['a', 'b', 'c']
def per(res, string, list):
	if len(list) == 1:
		res.append(string + list[0])
	else:
		for Tstr in list:
			Tlist = list[:]
			Tlist.remove(Tstr)
			per(res, string  + Tstr, Tlist)
	test = []

test = []
per(test, '', List)
for i in test:
	print(i)

res = []
def perNew(str, List):
	if len(List) == 1:
		res.append(str+List[0])
	else:
		for tempStr in List:
			tempList = List[:]
			tempList.remove(tempStr)
			perNew(str + tempStr, tempList)
	for obj in res:
		print(obj)

def perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

for item in list(perms('abc')):
    print(item)