import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context('paper')
sns.set_style('darkgrid')

labels = ['Not Taken', 'Taken', 'Bimod', '2lev', 'Combined Bimod & 2lev']

# Branch Address
bar1 = [41.02, 55.78, 53.13, 55.78, 56.85, 58.11]
bar2 = [75.37, 66.14, 68.91, 66.14, 66.49, 65.08]
bar3 = [71.48, 88.38, 91.47, 88.38, 89.78, 94.15]
bar4 = [65.74, 85.69, 89.71, 85.69, 88.73, 93.03]
bar5 = [73.24, 89.79, 92.45, 89.79, 92.60, 95.72]

# Branch Direction
# bar1 = [41.02, 55.78, 53.13, 55.78, 56.85, 58.11]
# bar2 = [75.37, 66.14, 68.91, 66.14, 66.49, 65.08]
# bar3 = [83.98, 91.16, 94.12, 91.16, 91.04, 94.72]
# bar4 = [77.96, 88.69, 92.42, 88.69, 90.16, 93.61]
# bar5 = [83.43, 92.15, 94.57, 92.15, 93.71, 96.27]

for n, bar in enumerate(zip(bar1, bar2, bar3, bar4, bar5)):
    fig, ax = plt.subplots(figsize=[15, 15])
    width = .5
    items = np.array(range(5))
    colors = ['#fa1900', '#00fa00', '#3a00fa', '#D800FF', '#FF6200']

    b1 = plt.bar(items[0], bar[0], width=width, align='center', label=labels[0], alpha=.8, color=colors[0])
    b2 = plt.bar(items[1], bar[1], width=width, align='center', label=labels[1], alpha=.8, color=colors[1])
    b3 = plt.bar(items[2], bar[2], width=width, align='center', label=labels[2], alpha=.8, color=colors[2])
    b4 = plt.bar(items[3], bar[3], width=width, align='center', label=labels[3], alpha=.8, color=colors[3])
    b5 = plt.bar(items[4], bar[4], width=width, align='center', label=labels[4], alpha=.8, color=colors[4])

    for i, v in enumerate(bar):
        plt.text(i - .08, v + 0.01, str(v), fontsize=18)

    plt.ylim([0, 100])
    plt.xticks([], [])
    plt.yticks(fontsize=22)
    plt.legend(fontsize=22, loc='upper right')
    plt.grid(True)

    plt.savefig('../figure1/branch address prediction/' + str(n + 1) + '.png', bbox_inches="tight", pad_inches=0)
    plt.savefig('../figure1/branch address prediction/' + str(n + 1) + '.eps', bbox_inches="tight", pad_inches=0)
