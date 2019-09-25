# -*- coding: utf-8 -*-
list1 = [1,2,3,4,5]
list2 = ["hello","world","!"]
list3 = [1, "hello", 9.99, True]

for i in list3:
	print(i)

for i in range(10,20,3):
	print(i)
	
list3.append("append word")	

if 5 in list1:
	print("present")

# sort ----
list5 = [3,7,1,90,45]
list5.sort(reverse=True)
print(list5)

