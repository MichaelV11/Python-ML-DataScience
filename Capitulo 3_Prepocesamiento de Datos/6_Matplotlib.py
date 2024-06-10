import matplotlib.pyplot as plt
import seaborn as sns

# Create a line plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
#plt.plot(x, y)
#plt.show()

plt.plot(x, y)
plt.title('Square Numbers')
plt.xlabel('Value')
plt.ylabel('Square')
plt.grid(True)
plt.show()