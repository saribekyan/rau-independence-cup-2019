# from UKIEPC 2019
# author Robin Lee

n,k = map(int, input().split())
items = list(map(int, input().split()))

residence = [i for i in range(n)]
knocks = [[0, i] for i in range(n)]
held = items[0]-1
for i in items[1:]:
  knocks[residence[i-1]][0] += 1
  residence[held] = residence[i-1]
  held = i-1

knocks = [(a, b) for a, b in knocks]
knocks = list(sorted(knocks, reverse=True))
knocks = [i for i in knocks if i[1]+1 != items[0]]

cost = sum([knocks[i][0] * (i+1) for i in range(len(knocks))])
knocks = [i[1]+1 for i in knocks if i[1]+1 != items[0]]

print(2 * cost)
# print(' '.join(map(str,knocks)))
