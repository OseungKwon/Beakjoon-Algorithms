n, m = map(int, input().split())

s = []
def solve(depth,n,m):
  if depth == m:
    print(' '.join(map(str, s)))

    return

  for i in range(1, n + 1):
    if i in s:
      continue
    s.append(i)
    solve(depth+1,n,m)
    s.pop()

solve(0,n,m)

