# -*- coding: utf-8 -*-

data_in = open("18s_human.fasta").read()
data_out = open("18s_human.html","w")

count = {}

for i in ['A', 'T', 'C', 'G']:
	for j in ['A', 'T', 'C', 'G']:
		count[i+j] = 0

data_in = data_in.replace("\n","")

for k in range(len(data_in)-1):
	count[data_in[k]+data_in[k+1]] += 1

# html

data_out.write("<div>")

i = 1
for k in count:
	mirror = count[k]/max(count.values())
	data_out.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(mirror)+"')>"+k+"</div>")

	if i%4 == 0:
		data_out.write("<div style='clear:both'></div>")

	i+=1

data_out.close()