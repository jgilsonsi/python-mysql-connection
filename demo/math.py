# -*- coding: utf-8 -*-
x = 2
y = 3

print(x == y)
print(x > y)
print(x ** y)
print(x % y)

print(x == y and y == 2)
print(x == y or y == 3)

if x < y:
	print("x é menor")
else:
	print("x é maior")

while x <= 10:
	print(x)
	x += 1