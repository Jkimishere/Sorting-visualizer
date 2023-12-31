import matplotlib.pyplot as plt
from matplotlib.widgets import Button,Slider 
import random
from sorter import quicksort
import threading
import psutil

DELAY_TIME = 0.1


def plot_values(values:list, title:str = 'Visualizing sorting algorithms', ):
    global DELAY_TIME
    print('starting plot')
    ax.clear()
    print('cleared')
    ax.bar(range(len(values)), values)
    ax.set_title(title) 
    plt.pause(DELAY_TIME)
    plt.ioff()
    plt.show(block=True)



def shuffle_values(event):
    global values
    random.shuffle(values)
    plot_values(values, 'Visualizing sorting algorithms')

def quicksort_values(event):
    global quicksort_button
    global shuffle_button
    global slider
    global values
    quicksort_button.active=False
    shuffle_button.active=False
    slider.active = False
    quicksort(values,0,len(values)-1, plot_values, fig.number)
    plot_values(values, 'Done quicksorting')
    quicksort_button.active=True
    shuffle_button.active=True
    slider.active = True

def change_length_values(val):
    global values
    print(val)
    values = list(range(val))
    plot_values(values)
values = list(range(1, 100))

fig, ax = plt.subplots()
bar_plot = ax.bar(range(len(values)), values)
ax.set_title('Visualizing sorting algorithms')


shuffle_button_ax = plt.axes([0.85, 0.01, 0.1, 0.05])  # [x, y, width, height]
shuffle_button = Button(shuffle_button_ax, 'Shuffle')
shuffle_button.on_clicked(shuffle_values)

quicksort_button_ax = plt.axes([0.72, 0.01, 0.1, 0.05])  # [x, y, width, height]
quicksort_button = Button(quicksort_button_ax, 'Quicksort')
quicksort_button.on_clicked(quicksort_values)

slider = Slider(plt.axes([0.1, 0.01, 0.4, 0.03]), 'Length of array:', 10, 100, valinit=100, valstep=1)
slider.on_changed(change_length_values)


# Display the plot


plt.show(block=True)


