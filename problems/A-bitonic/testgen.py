MAX_N   = 100000
MAX_H   = 1000000000
N_TESTS = 20

import os
import random

script_path = os.path.realpath(__file__)
dir_path    = os.path.dirname(script_path)
test_dir    = os.path.join(dir_path, '../../tests/A')

if not os.path.exists(test_dir):
    os.mkdir(test_dir)

curr_test = 1
def print_test(heights):
    global curr_test

    assert(curr_test <= N_TESTS)
    assert(len(heights) <= MAX_N)
    for h in heights:
        assert(1 <= h and h <= MAX_H)

    print('printing test %d' % curr_test)
    fname = os.path.join(test_dir, '%03d' % curr_test)
    with open(fname, 'w') as f:
        f.write('%d\n' % len(heights))
        f.write(' '.join([str(h) for h in heights]))
        f.write('\n')

    curr_test += 1

print_test([2, 1, 5, 3, 3])     # sample test 1
print_test([1, 2, 3, 4, 2, 1])  # sample test 2

print_test([1])

print_test([10] * 100) # constant sequence
print_test(list(range(1, 101))) # increasing
print_test(list(range(100, 0, -1))) # decreasing
print_test(list(range(10, 0, -1)) + list(range(1, 11))) # \/
print_test(list(range(1, 11)) + list(range(10, 0, -1))) # /\

while curr_test <= N_TESTS / 2:
    n = random.randint(1, 20000)
    heights = [ random.randint(1, 20000) for i in range(n) ]
    print_test(heights)

print_test([MAX_H] * MAX_N) # constant sequence
print_test(list(range(1, MAX_N + 1))) # increasing
print_test(list(range(MAX_N, 0, -1))) # decreasing
print_test(list(range(MAX_N / 2, 0, -1)) + list(range(1, MAX_N / 2 + 1))) # \/
print_test(list(range(1, MAX_N / 2 + 1)) + list(range(MAX_N / 2 + 100, 100, -1))) # /\

while curr_test <= N_TESTS:
    n = random.randint(1, MAX_N)
    heights = [ random.randint(1, MAX_H) for i in range(n) ]
    print_test(heights)

