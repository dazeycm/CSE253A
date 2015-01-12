# def swap(a, b):
# 	tmp = a
# 	a = b
# 	b = tmp
# 
# x = 4
# y = 5
# swap(x, y)
# print(x, y)
#OUTPUT: 4 5
#
# from test.test_wsgiref import hello_app
# import sys
# def f1(x):
#     x = x + "!"
# def f2(x):
#     x = x + 1	
# def f3(list):
# 	list = [1,2,3]
# def f4(list):
# 	list[0] = -100
# s1 = "hello"
# i1 = 34
# f1(s1)
# f2(i1)
# list1 = [0,1,2,3,4,5,6,7,8,9];
# list2 = [0,1,2,3,4,5,6,7,8,9];
# f3(list1);
# f4(list2)
# print(s1)
# print(i1)
# print(list1)
# print(list2)
#OUTPUT:
# hello
# 34
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [-100, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# def g(w, x):
# 	def f():
# 		nonlocal z
# 		global y
# 		w = 0
# 		x = 1
# 		y = 2
# 		z = 3
# 		print('F: ', w, x, y, z)
# 	z = True
# 	print('In G, before call to F: ', w, x, y, z)
# 	f()
# 	print('In G, after call to F: ', w, x, y, z)
# 	print()
# 
# w = 'a'
# x = 'b'
# y = 'c'
# z = 'd'
# print('In main, before call to G: ', w, x, y, z)
# g(w, x)
# print('In main, after call to G: ', w, x, y, z)
#OUTPUT: In main, before call to G: a b c d
# In G, before call to F: a b c True
# F: 0 1 2 3
# In G after call to F: a b 2 3
# In main, after call to G:  a b 2 d

def numContainingSubstring(base, *strings):
	count = 0;
	for str in strings:
		if base in str:
			count += 1
	return count

def computeDST(**variables):
	if 'speed' in variables and 'time' in variables:
		return variables['speed'] * variables['time']
	if 'time' in variables and 'distance' in variables:
		return variables['distance'] / variables['time']
	if 'distance' in variables and 'speed' in variables:
		return variables['distance'] / variables['speed']
