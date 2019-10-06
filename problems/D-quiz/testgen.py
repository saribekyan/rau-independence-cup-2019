N_TESTS = 20

NMAX = 1000

import os
import random

script_path = os.path.realpath(__file__)
dir_path    = os.path.dirname(script_path)
test_dir    = os.path.join(dir_path, '../../tests/D')

if not os.path.exists(test_dir):
    os.mkdir(test_dir)

curr_test = 1
def print_test(S):
    global curr_test
    assert(curr_test <= N_TESTS)

    in_fname = os.path.join(test_dir, '%03d' % curr_test)
    print in_fname

    assert(1 <= len(S) and len(S) <= NMAX)
    for c in S:
        assert(c.isdigit() or c == '?')

    assert(S[0] != '0')

    with open(in_fname, 'w') as f:
        f.write(S + '\n')

    curr_test += 1

def rand_question_marks(n, q):
    digits = [ str(random.randint(1, 9)) ]
    digits += [ str(random.randint(0, 9)) for i in range(1, n) ]
    for i in range(q):
        l = random.randint(0, n - 1)
        digits[l] = '?'

    for i in range(min(n, 3)):
        if random.randint(0, 2) == 0:
            digits[n - 1 - i] = '?'

    return ''.join(digits)

print_test('1?23')
print_test('3?2?')

print_test('1')
print_test('8')
print_test('?')

print_test('???')
print_test('????')

print_test('?????????????????1')

print_test('8' * NMAX)
print_test('1' * NMAX)

print_test(rand_question_marks(NMAX, NMAX / 2))

print_test('111111111111111111111111111111111111111111111111111111111???')

while curr_test <= N_TESTS:
    n = random.randint(1, NMAX)
    q = random.randint(1, n)
    print_test(rand_question_marks(n, q))

