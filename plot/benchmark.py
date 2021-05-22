import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context('paper')
sns.set_style('darkgrid')

labels = ['Total Number of Instructions', 'Total Number of Loads & Stores', 'Total Number of Branches']

bar1 = [7070, 43437, 20484, 7177, 189388, 1259872]
bar2 = [3906, 12334, 6502, 3960, 47619, 295673]
bar3 = [941, 7772, 3485, 988, 32161, 254445]

for n, bar in enumerate(zip(bar1, bar2, bar3)):
    fig, ax = plt.subplots(figsize=[15, 15])
    width = .5
    items = np.array(range(3))
    colors = ['#f70202', '#0b98d4', '#80d40b']

    b1 = plt.bar(items[0], bar[0], width=width, align='center', label=labels[0], alpha=.8, color=colors[0])
    b2 = plt.bar(items[1], bar[1], width=width, align='center', label=labels[1], alpha=.8, color=colors[1])
    b3 = plt.bar(items[2], bar[2], width=width, align='center', label=labels[2], alpha=.8, color=colors[2])

    for i, v in enumerate(bar):
        plt.text(i - .08, v + 0.01, str(v), fontsize=18)

    plt.xticks([], [])
    plt.yticks(fontsize=22)
    plt.legend(fontsize=22, loc='upper right')
    plt.grid(True)

    plt.savefig('../figure/benchmark/' + str(n + 1) + '.png', bbox_inches="tight", pad_inches=0)
    plt.savefig('../figure/benchmark/' + str(n + 1) + '.eps', bbox_inches="tight", pad_inches=0)
