import matplotlib.pyplot as plt
import random

values = list(range(100))
random.shuffle(values)

def update_plot(vals):
    ax.clear()
    ax.bar(range(len(values)), values)
    ax.set_ylabel('Values')
    ax.set_title('Sorting visualization')
    plt.draw()


fig, ax = plt.subplots()
bar_plot = ax.bar(range(len(values)), values)
ax.set_xlabel('Index')
ax.set_ylabel('Values')
ax.set_title('Sorting visualization')



import time
for i in range(10):
    print('asdfasdf')
    random.shuffle(values)
    update_plot(values)
    time.sleep(1)

    
plt.show()