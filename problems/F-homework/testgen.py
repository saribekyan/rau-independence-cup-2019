N_TESTS = 20

NMAX = 20
AMAX = 1000000000

import os
import random

script_path = os.path.realpath(__file__)
dir_path    = os.path.dirname(script_path)
test_dir    = os.path.join(dir_path, '../../tests/F')

if not os.path.exists(test_dir):
    os.mkdir(test_dir)

curr_test = 1
def print_test(N, A):
    global curr_test
    assert(curr_test <= N_TESTS)

    in_fname = os.path.join(test_dir, '%03d' % curr_test)
    print(in_fname)

    assert(1 <= N and N <= NMAX)
    assert(1 <= A and A <= AMAX)

    with open(in_fname, 'w') as f:
        f.write('%d %d\n' % (N, A))

    curr_test += 1

# sample
print_test(4, 22)
print_test(2, 1)

print_test(1, 1)
print_test(1, 2)

print_test(NMAX, AMAX)
print_test(NMAX, random.randint(1, 2 ** (NMAX - 1) - 1))

while curr_test <= N_TESTS:
    N = random.randint(1, NMAX)
    if curr_test % 4 != 0:
        A = random.randint(1, AMAX)
    else:
        A = random.randint(1, 2 ** (N - 1) - 1)
    print_test(N, A)

