n,m,v=map(int, input().split())
# n=정점의 개수, m=간선의 개수, v=시작할 정점의 번호

graph=[set([]) for _ in range(n+1)]
for _ in range(m):
    i,j=map(int,input().split())
    graph[i].add(j)
    graph[j].add(i)

def DFS(graph, start):
    visited=[]
    stack=[start]

    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            stack+=sorted(list(graph[node]-set(visited)),reverse=True)
    return visited

def BFS(graph, start):
    visited=[]
    queue=[start]

    while queue:
        node=queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue+=sorted(list(graph[node]-set(visited)))
    return visited

for i in list(DFS(graph,v)):
    print(i,end=' ')
print()
for i in list(BFS(graph,v)):
    print(i,end=' ')