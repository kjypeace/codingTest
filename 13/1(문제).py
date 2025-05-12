######################## 복습 때 마다, 풀어보는 칸 ##########################
#도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
# 4 4 2 1
# 1 2
# 1 3
# 2 3 
# 2 4
# 출력 예시
# 4

from collections import deque
n,m,k,x = 4,4,2,1
graph = [[] for _ in range(n+1)]
data_list = [[1,2],[1,3],[2,3],[2,4]]
for i in range(m):
    a,b = data_list[i]
    graph[a].append(b)
distance = [-1] * (n+1)
distance[x] = 0
q = deque([x])

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)  
check = False

for i in range(1,n+1):
    if distance[i] == k:
        check = True
if check == False:
    print(-1)
