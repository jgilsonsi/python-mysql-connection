# Brazilian Population Growth 1980-2016
# DataSus
import matplotlib.pyplot as plt

data = open("population.csv").readlines()

x = []
y = []

for i in range(len(data)):
	if i != 0:
		line = data[i].split(";")
		x.append(int(line[0]))
		y.append(int(line[1]))

plt.bar(x, y, color="#e4e4e4")
plt.plot(x, y, color='k', linestyle="--")

plt.title("Brazilian Population Growth 1980-2016")
plt.xlabel("Year")
plt.ylabel("Population x100.000.000")
plt.show()
plt.savefig("brazilian_population.png", dpi=300)

