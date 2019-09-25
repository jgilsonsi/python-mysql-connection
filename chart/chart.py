# Python data view

import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7]
y1 = [2, 3, 7, 6]

x2 = [2, 4, 6, 8]
y2 = [3, 3, 10, 7]

title = "Bar chart"
x_title = "X title"
y_title = "Y title"

# Legend
plt.title(title)
plt.xlabel(x_title)
plt.ylabel(y_title)

plt.bar(x1, y1, label = "Group 1")
plt.bar(x2, y2, label = "Group 2")
plt.legend()
plt.show()