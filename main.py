#Importing libraries

import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
import random
from sorter import quicksort

#Modify if needed
DELAY_TIME = 0.1
BASE_COLOR = ['#5b92c9']
COLORS_BASE = BASE_COLOR * 50
SORT_ALGORITHM_LIST = ['Quick', 'Insertion']


# Function to plot the list
def plot_values(values, title='Visualizing sorting algorithms', colors=None):
    """
    Function to plot values on the plot.

    Parameters:
    - values (list) : List of the values to be plotted
    - title (str) : Title of the plot
    - colors (list) : The colors of the bars

    Raises:
    - ValueError : If length of values and colors are different.
    """


    c = colors if colors is not None else COLORS_BASE
    if len(values) != len(c):
        print(len(values), len(c))
        raise ValueError("Length of 'values' and 'colors' must be the same.")
    ax.clear()
    ax.bar(range(len(values)), values, color=c)
    ax.set_title(title)
    plt.pause(DELAY_TIME)
    plt.show(block=True)

def shuffle_values(event):
    """
    Shuffles the values and plots them.
    """
    global values
    random.shuffle(values)
    plot_values(values, 'Visualizing sorting algorithms')


# Event handler to perform quicksort on values
def quicksort_values(event):
    global quicksort_button, shuffle_button, slider, values
    quicksort_button.active = shuffle_button.active = slider.active = False
    quicksort(values, 0, len(values) - 1, plot_values, fig.number)
    plot_values(values, 'Done quicksorting')
    quicksort_button.active = shuffle_button.active = slider.active = True

# Event handler to change length of the list
def change_length_values(val):
    global values, BASE_COLOR, COLORS_BASE
    values = list(range(val + 1))
    COLORS_BASE = BASE_COLOR * (val + 1)
    plot_values(values)


# Initial values for the array
values = list(range(1, 51))

# Create plot
fig, ax = plt.subplots()
ax.bar(range(len(values)), values, color=COLORS_BASE)
ax.set_title('Visualizing sorting algorithms')


# UI code
shuffle_button_ax = plt.axes([0.85, 0.01, 0.1, 0.05])
shuffle_button = Button(shuffle_button_ax, 'Shuffle')
shuffle_button.on_clicked(shuffle_values)

quicksort_button_ax = plt.axes([0.72, 0.01, 0.1, 0.05])
quicksort_button = Button(quicksort_button_ax, 'Quicksort')
quicksort_button.on_clicked(quicksort_values)

slider = Slider(plt.axes([0.1, 0.01, 0.4, 0.03]), 'Length of array:', 10, 100, valinit=50, valstep=1)
slider.on_changed(change_length_values)

# Show the plot
plt.show(block=True)
