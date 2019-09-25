# -*- coding: utf-8 -*-

file = open("file.txt")

lines = file.readlines()
all_text = file.read()

print(lines)

w = open("file2.txt","w")
w.write("That is my second file")
w.close()