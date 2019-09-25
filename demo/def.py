def soma(x, y):
	return x + y

s = soma(2, 3)
print(s)

try:
	print(5/0)
except Exception as e:
	print("Not allowed")


# statistics: 
#from statistics import *
#mean(list1)
#median(list1)
#mode(list1)