import sys
INF = sys.maxsize

def Warshall():
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = arr[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
n = 4 # 정점 수
arr = [[0, 2, INF, 4], [2, 0, INF, 5], [3, INF, 0, INF], [INF, 2, 1, 0]]
dist = Warshall()

for i in range(n):
    for j in range(n):
        print(dist[i][j], end=' ')
    print()