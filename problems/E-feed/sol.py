import sys

# essentially need to find the sizes of the
# components that one gets after applying the mask

# each component with k nodes has k(k+1)/2 paths.
def count_at_least_mask(g, V, mask):
    n = len(g)

    parent = [None] * n

    answer = 0

    for v in range(n):
        if (parent[v] is None) and (V[v] & mask) == mask:

            comp_size = 1

            stack = [ ]
            stack.append((v, 0))
            parent[v] = -1

            while len(stack) > 0:
                u, i = stack.pop()

                while i < len(g[u]):
                    if (V[g[u][i]] & mask) == mask and g[u][i] != parent[u]:
                        break
                    i += 1

                if i == len(g[u]):
                    continue

                parent[g[u][i]] = u

                stack.append((u, i + 1))
                stack.append((g[u][i], 0))
                comp_size += 1

            answer += comp_size * (comp_size + 1) / 2

    return answer

# we will solve using inclusion-exclusion, as we did in the
# original version of the problem. This has complexity
# O(n2^K + 2^(2K)). Another way of doing it is to calculate for each
# mask the number of paths exactly using DP rather than inclusion
# inclusion-exclusion, but that gives runtime O(n2^(2K)). It's still
# ok, but I already had the inc-exc written.
def n_paths_at_least_L_zeros(g, masks, K, L):
    n = len(g)

    mask_count_at_least = [None] * (1 << K)
    for mask in range(1 << K):
        mask_count_at_least[mask] = count_at_least_mask(g, masks, mask)

    mask_count_exact = [0] * (1 << K)
    for mask in range(1 << K):
        for t in range(mask, 1 << K):
            if (mask & t) == mask:
                diff = t ^ mask
                parity = 0
                while diff != 0:
                    parity ^= (diff & 1)
                    diff >>= 1

                if parity == 0:
                    mask_count_exact[mask] += mask_count_at_least[t]
                else:
                    mask_count_exact[mask] -= mask_count_at_least[t]

    answer = 0
    for mask in range(1 << K):
        k = 0
        m = mask
        while m != 0:
            k += (m & 1)
            m >>= 1

        if k <= K - L: # at most K - L ones
            answer += mask_count_exact[mask] 

    return answer

def line2int():
    return list(map(int, sys.stdin.readline().split()))

if __name__ == '__main__':
    n, K, L = line2int()

    masks = [ int(sys.stdin.readline().strip(), 2) for i in range(n)]
    masks = [ ((1 << K) - 1) ^ m for m in masks ]

    g = [ [ ] for i in range(n) ]
    for i in range(n - 1):
        u, v = line2int()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    print(n_paths_at_least_L_zeros(g, masks, K, L))

