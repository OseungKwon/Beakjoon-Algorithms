n, m = map(int, input().split())

s = []
count=0
def solve(depth,count,n,m):
  if depth == m:
    print(' '.join(map(str, s)))
    return
  for i in range(count, n + 1):
    s.append(i)
    solve(depth+1,count,n,m)
    count += 1
    s.pop()
solve(0,1,n,m)