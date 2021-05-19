import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context('paper')
sns.set_style('darkgrid')

labels = ['Total Number of Instructions', 'Total Number of Loads & Stores', 'Total Number of Branches']

bar1 = [7070, 43437, 20484, 7177, 189388, 1259872]
bar2 = [3906, 12334, 6502, 3960, 47619, 295673]
bar3 = [941, 7772, 3485, 988, 32161, 254445]

fig, ax = plt.subplots(figsize=[25, 10])
height = .275
items = np.array(range(6))
colors = ['#f70202', '#0b98d4', '#80d40b']
plt.barh(items - height, bar1, height=height, label=labels[0], alpha=.8, log=True, color=colors[0])
plt.barh(items, bar2, height=height, label=labels[1], alpha=.8, log=True, color=colors[1])
plt.barh(items + height, bar3, height=height, label=labels[2], alpha=.8, log=True, color=colors[2])

plt.ylabel('Benchmarks', fontsize=20)
benchmarks = ['Anagram', 'Test-fmath', 'Test-llong', 'Test-lswlr', 'Test-math', 'Test-printf']
plt.yticks([r + height for r in range(len(bar1))], benchmarks, fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.legend(fontsize=20, loc='lower right')
ax.set_xscale('log')
plt.grid(True, which="both", linestyle='--')

plt.savefig('../figure/benchmark-detail.png')
plt.savefig('../figure/benchmark-detail.eps')
plt.show()
