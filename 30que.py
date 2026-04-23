#Write a program using matplotlib to plot line and bar graphs.

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 1. Line Graph
plt.figure()
plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 2. Bar Graph
categories = ["A", "B", "C", "D", "E"]
values = [5, 7, 3, 8, 6]

plt.figure()
plt.bar(categories, values)
plt.title("Bar Graph")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()