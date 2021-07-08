n, m = map(int, input().split())

s = []
count=0
def solve(depth,idx,n,m):
  if depth == m:
    print(' '.join(map(str, s)))
    return

  for i in range(idx, n + 1):
    if i in s:
      continue
    s.append(i)
    solve(depth+1,i+1,n,m)
    s.pop()

solve(0,1,n,m)

