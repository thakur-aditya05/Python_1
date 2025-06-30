import matplotlib.pyplot as plt

colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'black', 'white']

plt.bar(range(len(colors)), [1]*len(colors), color=colors)
plt.show()