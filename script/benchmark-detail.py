benchmarks = ['anagram', 'test-fmath', 'test-llong', 'test-lswlr', 'test-math', 'test-printf']

n_instruction = []
n_load_store = []
n_branches = []

for i, benchmark in enumerate(benchmarks):

    with open('../data/' + benchmark + '_6' + '.txt', 'r') as f:
        lines = f.readlines()

    lines = [line.strip().split() for line in lines]

    for line in lines:
        if ' '.join(line[-5:]) == 'total number of instructions executed':
            address_pred_acc = int(line[-7])
            n_instruction.append(address_pred_acc)

        if ' '.join(line[-7:]) == 'total number of loads and stores executed':
            direction_pred_acc = int(line[-9])
            n_load_store.append(direction_pred_acc)

        if ' '.join(line[-5:]) == 'total number of branches executed':
            direction_pred_acc = int(line[-7])
            n_branches.append(direction_pred_acc)

print('bar1 =', n_instruction)
print('bar2 =', n_load_store)
print('bar3 =', n_branches)
