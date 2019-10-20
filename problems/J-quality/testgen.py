N_TESTS = 24

NMAX = 10 ** 9
KXMAX = 40

import os
import random
import string

script_path = os.path.realpath(__file__)
dir_path    = os.path.dirname(script_path)
test_dir    = os.path.join(dir_path, '../../tests/J')

if not os.path.exists(test_dir):
    os.mkdir(test_dir)

curr_test = 1
def print_test(N, XA, KA, XV, KV):
    global curr_test
    assert(curr_test <= N_TESTS)

    in_fname = os.path.join(test_dir, '%03d' % curr_test)
    print(in_fname)

    assert(1 <= N and N <= NMAX)
    
    for x in XA + XV:
        assert(x in string.ascii_lowercase)

    assert(KA * len(XA) <= KXMAX)
    assert(KV * len(XV) <= KXMAX)

    with open(in_fname, 'w') as f:
        f.write('%d\n' % N)
        f.write('%s %d\n' % (XA, KA))
        f.write('%s %d\n' % (XV, KV))

    curr_test += 1

def rand_str(k, unique_letters=26):
    letters = set()
    while len(letters) < unique_letters:
        letters.add(string.ascii_lowercase[random.randint(0, 25)])
    letters = list(letters)

    return ''.join([random.choice(letters) for i in range(k)])

# sample
print_test(3, 'aa', 1, 'aa', 1)
print_test(10, 'aaa', 5, 'bbb', 5)

# small edge cases
print_test(100, 'x', 16, 'y', 16)
print_test(1, 'abcd', 16 // 4, 'qwer', 16 // 4)
print_test(100, 'a', 1, 'b', 1)
print_test(100, rand_str(16), 1, rand_str(16), 1)
print_test(100, rand_str(16, 1), 1, rand_str(16, 1), 1)

# small random
while curr_test <= N_TESTS // 2:
    n = random.randint(1, 1000)
    ka = random.randint(1, 16)
    xa = rand_str(16 // ka, random.randint(1, 26))
    kv = random.randint(1, 16)
    xv = rand_str(16 // kv, random.randint(1, 26))

    print_test(n, xa, ka, xv, kv)

# edge cases
print_test(NMAX, 'x', KXMAX, 'y', KXMAX)
print_test(1, 'abcdefgh', KXMAX // 8, 'qwertyui', KXMAX // 8)
print_test(NMAX, 'a', 1, 'b', 1)
print_test(NMAX, rand_str(KXMAX), 1, rand_str(KXMAX), 1)
print_test(NMAX, rand_str(KXMAX, 1), 1, rand_str(KXMAX, 1), 1)

# random
while curr_test <= N_TESTS:
    n = random.randint(1, NMAX)
    ka = random.randint(1, KXMAX)
    xa = rand_str(KXMAX // ka, random.randint(1, 26))
    kv = random.randint(1, KXMAX)
    xv = rand_str(KXMAX // kv, random.randint(1, 26))

    print_test(n, xa, ka, xv, kv)

