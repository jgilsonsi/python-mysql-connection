import matplotlib.pyplot as plt
 
x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 3300, 100]
 
title = "Scatterplot"
xline = "X Line"
yline = "Y Line"
 
# Legends
plt.title(title)
plt.xlabel(xline)
plt.ylabel(yline)
 
plt.plot(x, y, color="#000000", linestyle="--")
plt.scatter(x, y, label="My label", color="y", marker=".", s=z)
plt.legend()
#plt.show()
plt.savefig("chart.pdf")
plt.savefig("chart.png", dpi=300)