import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import random
from sorter import quicksort

def shuffle_values(event):
    global values
    random.shuffle(values)
    ax.clear()
    ax.bar(range(len(values)), values)
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.set_title('Shuffled Bar Chart')
    plt.draw()


values = list(range(1, 100))

fig, ax = plt.subplots()
bar_plot = ax.bar(range(len(values)), values)
ax.set_xlabel('Index')
ax.set_ylabel('Values')
ax.set_title('Bar Chart with Shuffle Button')

# Adding the shuffle button
shuffle_button_ax = plt.axes([0.85, 0.01, 0.1, 0.05])  # [x, y, width, height]
shuffle_button = Button(shuffle_button_ax, 'Shuffle')
shuffle_button.on_clicked(shuffle_values)

# Display the plot
plt.show()