N_TESTS = 100

NMIN = 100
NMAX = 1000
XMAX = 1000000000

import os
import random
import math

script_path = os.path.realpath(__file__)
dir_path    = os.path.dirname(script_path)
test_dir    = os.path.join(dir_path, '..//..//tests//C')

if not os.path.exists(test_dir):
    os.mkdir(test_dir)

curr_test = 1
def print_test(Delta):
    global curr_test
    assert(curr_test <= N_TESTS)

    in_fname = os.path.join(test_dir, '%03d' % curr_test)
    ans_fname = os.path.join(test_dir, '%03d.a' % curr_test)
    print(in_fname)

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
    deltaMax = XMAX // n
    Delta = [ None ] * n
    for i in range(n):
        Delta[i] = random.randint(-deltaMax, deltaMax)
    return Delta

def powertwo_plus_one(n):
    deltaMax = XMAX // n
    l = int(math.log(deltaMax, 2))

    Delta = [ None ] * n
    for i in range(n):
        Delta[i] = (1 << (2 * random.randint(0, l // 2) + 1)) + 1
    return Delta

def power_plus_one(p):
    n = random.randint(NMIN, NMAX)
    deltaMax = XMAX // n
    l = int(math.log(deltaMax, p))

    Delta = [ None ] * n
    for i in range(n):
        Delta[i] = (p ** (2 * random.randint(0, l // 2) + 1)) + 1
    return Delta

def negate(Delta):
    return [-d for d in Delta]

def randSign(Delta):
    return [ random.choice([-1, 1]) * x for x in Delta ]

def powertwoDelta_plus_one(n):
    deltaMax = XMAX // n
    Delta = [ ]

    for i in range(n):
        delta = 0
        x = 1
        prev = 0
        while delta > -deltaMax:
            prev = delta
            delta += x
            x *= -2
            delta += x
            x *= -2
            if random.randint(0, 5) == 0:
                break
        Delta.append(prev - 1)

    return Delta

def powerDelta_plus_one(p):
    n = random.randint(NMIN, NMAX)
    deltaMax = XMAX // n
    Delta = [ ]

    for i in range(n):
        delta = 0
        x = 1
        prev = 0
        while delta > -deltaMax:
            prev = delta
            delta += x
            x *= -p
            delta += x
            x *= -p
            if random.randint(0, 5) == 0:
                break
        Delta.append(prev - 1)

    return Delta


def alternate(Delta, sign):
    for i in range(len(Delta)):
        Delta[i] = sign * Delta[i]
        sign *= -1
    return Delta

print_test([ 1 ] * NMIN)
print_test([ -1 ] * NMIN)

print_test(randSign([ XMAX // NMAX ] * NMAX))

print_test(rand_test(NMIN))

for it in range(2):
    for gen in [power_plus_one, powerDelta_plus_one]:
        for p in range(2, 6):
            for flip in [lambda x : alternate(x, -1), lambda x : alternate(x, 1), negate, (lambda x : x)]:
                print_test(flip(gen(p)))

n = random.randint(NMAX, NMAX)
deltaMax = XMAX // n
print_test([random.randint(-deltaMax, deltaMax)] * n)
print_test([random.randint(-deltaMax, deltaMax)] * n)

n = random.randint(NMAX, NMAX)
deltaMax = XMAX // n
print_test([random.randint(-deltaMax, deltaMax)] * n)
print_test([random.randint(-deltaMax, deltaMax)] * n)

