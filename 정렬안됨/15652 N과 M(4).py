n, m = map(int, input().split())
s = []

empty=[]
count=0
def solve(depth,count,m):
  if depth == m:
    print(' '.join(map(str, s)))
    return
  for i in range(count, n + 1):
    s.append(i)
    solve(depth+1,count,m)
    count += 1
    s.pop()
solve(0,1,m)