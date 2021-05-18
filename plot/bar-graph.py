import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context('paper')
sns.set_style('darkgrid')

labels = ['Strategy 6', 'Strategy 7', 'Novel Proposed Strategy']
width = 0.25

bar1 = [61.64, 47.41, 67.63, 62.96, 40.66, 54.58]
bar2 = [50.58, 46.62, 64.85, 52.23, 36.96, 41.97]
bar3 = [50.9, 49.54, 66.2, 52.02, 38.79, 42.42]

# Set position of bar on X axis
r1 = np.arange(len(bar1))
r2 = [x + width for x in r1]
r3 = [x + width for x in r2]

plt.figure(figsize=[25, 10])
plt.bar(r1, bar1, width=width, edgecolor='white', label=labels[0], alpha=.8, color=plt.get_cmap('plasma').colors)
plt.bar(r2, bar2, width=width, edgecolor='white', label=labels[1], alpha=.8)
plt.bar(r3, bar3, width=width, edgecolor='white', label=labels[2], alpha=.8)

plt.xlabel('Benchmarks', fontsize=18)
benchmarks = ['Anagram', 'Test-fmath', 'Test-llong', 'Test-lswlr', 'Test-math', 'Test-printf']
plt.ylim([0, 80])
plt.xticks([r + width for r in range(len(bar1))], benchmarks, fontsize=18)
plt.yticks(fontsize=18)
plt.legend(fontsize=18)
plt.grid('on')
xlocs, _ = plt.xticks()
print(xlocs)
for i, v in enumerate(bar1):
    plt.text(xlocs[i] - 0.38, v + 0.01, str(v), fontsize=16)

for i, v in enumerate(bar2):
    plt.text(xlocs[i] - 0.12, v + 0.01, str(v), fontsize=16)

for i, v in enumerate(bar3):
    plt.text(xlocs[i] + 0.14, v + 0.01, str(v), fontsize=16)

plt.title('Branch Address Prediction Rate (%)', fontsize=22)
plt.savefig('../figure/address-prediction-rate.png')
plt.savefig('../figure/address-prediction-rate.eps')
plt.show()
