import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context('paper')
sns.set_style('darkgrid')

labels = ['Strategy 6', 'Strategy 7', 'Proposed Strategy']

bar1 = [82.47, 73.92, 85.37, 82.29, 71.96, 77.04]
bar2 = [70.14, 74.7, 82.18, 71.76, 67.25, 65.28]
bar3 = [70.24, 77.26, 83.67, 71.56, 71.49, 65.55]

for n, bar in enumerate(zip(bar1, bar2, bar3)):
    fig, ax = plt.subplots(figsize=[15, 15])
    width = .5
    items = np.array(range(3))
    colors = ['#fa1900', '#00fa00', '#3a00fa']

    b1 = plt.bar(items[0], bar[0], width=width, align='center', label=labels[0], alpha=.8, color=colors[0])
    b2 = plt.bar(items[1], bar[1], width=width, align='center', label=labels[1], alpha=.8, color=colors[1])
    b3 = plt.bar(items[2], bar[2], width=width, align='center', label=labels[2], alpha=.8, color=colors[2])

    for i, v in enumerate(bar):
        plt.text(i - .08, v + 0.01, str(v), fontsize=18)

    plt.ylim([0, 100])
    plt.xticks([], [])
    plt.yticks(fontsize=22)
    plt.legend(fontsize=22, loc='upper right')
    plt.grid(True)

    plt.savefig('../figure/branch direction prediction/' + str(n + 1) + '.png', bbox_inches="tight", pad_inches=0)
    plt.savefig('../figure/branch direction prediction/' + str(n + 1) + '.eps', bbox_inches="tight", pad_inches=0)
