N_TESTS = 25

NMIN = 100
NMAX = 1000
XMAX = 1000000000

import os
import random
import math

script_path = os.path.realpath(__file__)
dir_path    = os.path.dirname(script_path)
test_dir    = os.path.join(dir_path, '../../tests/C')

if not os.path.exists(test_dir):
    os.mkdir(test_dir)

curr_test = 1
def print_test(Delta):
    global curr_test
    assert(curr_test <= N_TESTS)

    in_fname = os.path.join(test_dir, '%03d' % curr_test)
    ans_fname = os.path.join(test_dir, '%03d.a' % curr_test)
    print in_fname

    n = len(Delta)
    assert(NMIN <= n and n <= NMAX)

    X = [ Delta[0] ] * n
    for i in range(1, n):
        X[i] = X[i - 1] + Delta[i]
        assert(abs(X[i]) <= XMAX)

    with open(in_fname, 'w') as f:
        f.write('%d\n' % len(X))


    with open(ans_fname, 'w') as f:
        for x in X:
            f.write('%d\n' % x);

    curr_test += 1

def rand_test(n):
    deltaMax = XMAX / n
    Delta = [ None ] * n
    for i in range(n):
        Delta[i] = random.randint(-deltaMax, deltaMax)
    return Delta

def powertwo_plus_one(n):
    deltaMax = XMAX / n
    l = int(math.log(deltaMax, 2))

    Delta = [ None ] * n
    sign = 1
    for i in range(n):
        Delta[i] = sign * ((1 << random.randint(0, l)) + 1)
        sign *= -1
    return Delta

def negate(Delta):
    return [-d for d in Delta]

def randSign(Delta):
    return [ random.choice([-1, 1]) * x for x in Delta ]

print_test([ 1 ] * NMIN)
print_test([ -1 ] * NMIN)

print_test(randSign([ XMAX / NMAX ] * NMAX))

print_test(rand_test(NMAX))
print_test(rand_test(NMIN))

print_test(powertwo_plus_one(NMIN))
print_test(powertwo_plus_one(NMAX))

print_test(negate(powertwo_plus_one(NMIN)))
print_test(negate(powertwo_plus_one(NMAX)))

print_test(randSign(powertwo_plus_one(NMIN)))
print_test(randSign(powertwo_plus_one(NMAX)))

while curr_test <= N_TESTS:
    n = random.randint(NMIN, NMAX)

    ch = curr_test % 6

    deltaMax = XMAX / n

    if ch == 0:
        print_test([random.randint(-deltaMax, deltaMax)] * n)
    elif ch == 1:
        print_test(rand_test(n))
    elif ch == 2:
        print_test(powertwo_plus_one(n))
    elif ch == 3:
        print_test(negate(powertwo_plus_one(n)))
    elif ch == 4:
        print_test(randSign(powertwo_plus_one(n)))
    elif ch == 5:
        print_test(randSign([ random.randint(-deltaMax, deltaMax) ] * n)) 

