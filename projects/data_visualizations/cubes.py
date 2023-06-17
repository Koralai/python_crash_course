import matplotlib.pyplot as plt
import matplotlib as mpl

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

# Access the "cool" colormap
cool = mpl.colormaps['cool']

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=cool, s=5)

# Set chart title and label axes
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubed Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=10)

# Set the range for each axis
ax.axis([0, 5_001, 0, 125_000_000_000])

plt.show()
