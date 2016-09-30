# -*- coding: utf-8 -*-

# 2016年9月27日21:29:31
# http://python.jobbole.com/86495/
# 272

# 1 交换排序
# 1.1 冒泡
def maopao(array):
	"""有几个数 即有 几趟比较"""
	"""针对其中一个数 比较 他要和 其他 n-1 个进行比较 固定好 最大 OR 最小 那个数"""
	"""之后对其他数进行 比较 他要和 除了比较好的 数之外的数进行比较"""
	for n in range(len(array)-1)[::-1]:
		for i in range(n):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
	return array
# 1.2 快排
def kuaipai(array, left, right):
	"""通过一趟排序将待排的分割场独立的两部分"""
	if left >= right:
		return array
	pivokey = array[left]
	low = left
	high = right
	while left < right:
		while left < right and array[right] >= pivokey:
			right -= 1
		array[left] = array[right]
		while left < right and array[left] <= pivokey:
			left += 1
		array[right] = array[left]
	array[right] = pivokey
	kuaipai(array, low, left-1)
	kuaipai(array, left+1, high)
	return array
# 2 插入排序
# 2.1 直接插排
def zhicha(array):
	
# 2.2 希尔排序
# 3 选择排序
# 3.1 简单排序