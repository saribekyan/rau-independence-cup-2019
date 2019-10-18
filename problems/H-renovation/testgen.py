N_TESTS = 20

NMAX = 100000
MMAX = 100000

import os
import random

script_path = os.path.realpath(__file__)
dir_path    = os.path.dirname(script_path)
test_dir    = os.path.join(dir_path, '../../tests/H')

if not os.path.exists(test_dir):
    os.mkdir(test_dir)

curr_test = 1
def print_test(n, S):
    global curr_test
    assert(curr_test <= N_TESTS)

    in_fname = os.path.join(test_dir, '%03d' % curr_test)
    print(in_fname)

    m = len(S)
    assert(1 <= m and m <= MMAX)
    y = 0
    for x in S:
        assert(1 <= x and x <= n)
        assert(y != x)
        y = x

    with open(in_fname, 'w') as f:
        f.write('%d %d\n' % (n, m))
        f.write(' '.join(map(str, S)) + '\n')

    curr_test += 1

def print_rand_test(n, m):
    res = [ ]
    while len(res) < m:
      x = random.randint(1, n)
      if len(res) == 0 or res[-1] != x:
        res += [x]

    print_test(n, res)

# sample tests
print_test(3, [ 1, 3, 2, 3, 2 ])
print_test(5, [ 1, 4, 2, 3, 5, 2, 5, 2, 5 ])

# random tests

while curr_test <= N_TESTS / 2:
    if curr_test % 2 == 0:
        print_rand_test(random.randint(1, 10000), random.randint(1, 10000))
    else:
        print_rand_test(random.randint(1, 1000), random.randint(1, 100000))

while curr_test <= N_TESTS - 2:
    if curr_test % 2 == 0:
        print_rand_test(random.randint(1, NMAX / 10), random.randint(1, MMAX))
    else:
        print_rand_test(random.randint(1, NMAX), random.randint(1, MMAX))

print_rand_test(NMAX / 10, MMAX)
print_rand_test(NMAX, MMAX)

