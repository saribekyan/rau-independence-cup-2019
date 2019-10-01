MAX_N   = 10000
N_TESTS = 20

import os
import random

script_path = os.path.realpath(__file__)
dir_path    = os.path.dirname(script_path)
test_dir    = os.path.join(dir_path, 'tests')

if not os.path.exists(test_dir):
    os.mkdir(test_dir)

curr_test = 1
def print_test(n):
    global curr_test

    fname = os.path.join(test_dir, '%03d' % curr_test)
    with open(fname, 'w') as f:
        f.write('%d\n' % n)

    curr_test += 1

print_test(3) # sample test

print_test(1)
print_test(2)
print_test(MAX_N)

while curr_test <= N_TESTS:
    n = random.randint(1, MAX_N)
    print_test(n)

