n=int(input())
arr=[list(map(int,input().split())) for _ in range(4)]
print(arr)
team_set={i for i in range(n)}
s=[]
empty=[]
def solve(depth,count):
  if depth == 2:
    empty.extend(s)
    return
  for i in range(count, n):
    if i in s:
      continue
    s.append(i)
    solve(depth+1,count)
    #count += 1
    s.pop()
solve(0,0)
team=[empty[i:i + 2] for i in range(0, len(empty), 2)]
print(team)
