N_TESTS = 20

NMAX = 100000
WMAX = 10000

import os
import random

script_path = os.path.realpath(__file__)
dir_path    = os.path.dirname(script_path)
test_dir    = os.path.join(dir_path, '../../tests/K')

if not os.path.exists(test_dir):
    os.mkdir(test_dir)

curr_test = 1
def print_test(W):
    global curr_test
    assert(curr_test <= N_TESTS)

    in_fname = os.path.join(test_dir, '%03d' % curr_test)
    print(in_fname)

    n = len(W)
    assert(1 <= n and n <= NMAX)
    for w in W:
        assert(-WMAX <= w and w <= WMAX)

    with open(in_fname, 'w') as f:
        f.write('%d\n' % n)
        f.write(' '.join(list(map(str, W))) + '\n')

    curr_test += 1

def randtest(n, wmax = WMAX):
    return [ random.randint(-wmax, wmax) for i in range(n) ]

def oscilating(n, wmax=WMAX, step=1):
    v = random.randint(-wmax + step, wmax - step)
    d = step
    W = [ ]
    for i in range(n):
        W.append(v)
        v += step
        if v <= -wmax or v >= wmax:
            step *= -1
    return W

def add(W1, W2):
    return [ a + b for (a, b) in zip(W1, W2) ]

# sample tests
print_test([3, -2, 1, -4, 5, 2])
print_test([1, 2, 3, 2, 1])

# small edge tests
print_test([0])
print_test([ WMAX ] * 100)
print_test([ WMAX, -WMAX ] * 100) 

# small random tests
while curr_test <= N_TESTS // 2:
    n = random.randint(1, 2000)
    if curr_test % 3 == 0:
        print_test(randtest(n))
    elif curr_test % 3 == 1:
        print_test(oscilating(n, 100, 5))
    else:
        print_test(add(oscilating(n, 100, 5), randtest(n, 200)))

# large edge tests
print_test([0] * NMAX)
print_test([WMAX] * NMAX)
print_test([WMAX, -WMAX] * (NMAX // 2))

# large random tests
while curr_test <= N_TESTS:
    if curr_test <= N_TESTS - 3:
        n = random.randint(1, NMAX)
    else:
        n = NMAX
    if curr_test % 3 == 0:
        print_test(randtest(n))
    else:
        W = oscilating(n, WMAX * 4 // 5, random.randint(1, 100))
        if curr_test % 3 == 2:
            W = add(W, randtest(n, WMAX // 10))
        print_test(W)

