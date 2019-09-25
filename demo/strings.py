# -*- coding: utf-8 -*-

a = "José"
b = "Gilson"

concat = a + " " + b
print(concat)
print(len(concat))

print(a[2])
print(a[2:4])
print(b.upper())

string = "The next season"
text_list = string.split(" ")
print(text_list)
print(string.find("season"))

string = string.replace("next", "next life is a")
print(string)

concat = concat + "\n"
print(concat.strip()) #to remove special characters