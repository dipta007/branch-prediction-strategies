benchmarks = ['anagram', 'test-fmath', 'test-llong', 'test-lswlr', 'test-math', 'test-printf']

for i, strategy in enumerate(['6', '7', 'sms'], 1):

    address_pred_acc = 0
    direction_pred_acc = 0
    add_out = []
    dir_out = []

    for benchmark in benchmarks:
        with open('../data/' + benchmark + '_' + strategy + '.txt', 'r') as f:
            lines = f.readlines()

        lines = [line.strip().split() for line in lines]

        for line in lines:
            if ' '.join(line[-5:]) == 'branch address-prediction rate (i.e., addr-hits/updates)':
                address_pred_acc = round(float(line[-7]) * 100, 2)
                add_out.append(address_pred_acc)

            if ' '.join(line[-5:]) == 'branch direction-prediction rate (i.e., all-hits/updates)':
                direction_pred_acc = round(float(line[-7]) * 100, 2)
                dir_out.append(direction_pred_acc)

    print('bar' + str(i) + ' =', add_out)
