benchmarks = ['anagram', 'test-fmath', 'test-llong', 'test-lswlr', 'test-math', 'test-printf']

strategy = 'sms'

for benchmark in benchmarks:
    with open('../data/' + benchmark + '_' + strategy + '.txt', 'r') as f:
        lines = f.readlines()

    lines = [line.strip().split() for line in lines]

    hits = 0
    misses = 0
    lookup = 0

    for line in lines:
        if ' '.join(line[-7:]) == 'total number of direction-predicted hits (includes addr-hits)':
            hits = line[-9]

        if ' '.join(line[-4:]) == 'total number of misses':
            misses = line[-6]

        if ' '.join(line[-5:]) == 'total number of bpred lookups':
            lookup = line[-7]

    hits = int(hits)
    misses = int(misses)
    lookup = int(lookup)
    print(benchmark, '& {0} & {1} & {2} & {3:.2f}'.format(hits, misses, lookup, float(hits) / float(lookup) * 100))
