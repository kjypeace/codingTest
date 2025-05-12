# 4 4 2 1
# 1 2
# 1 3
# 2 3 
# 2 4

from collections import deque
# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
# n, m, k, x = map(int, input().split())
n, m, k, x = 4, 4, 2, 1
graph = [[] for _ in range(n + 1)]
data_list = [[1,2],[1,3],[2,3],[2,4]]
# 모든 도로 정보 입력 받기
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
for i in range(m):
    a, b = data_list[i]
    graph[a].append(b)
# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정
print("distance :",distance)
print(distance,"[",x,"] :",distance[x])
print("graph :",graph)
# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    print("\n")
    print("########################## while q 시작 ########################")
    print("q :",q)
    now = q.popleft()
    print("now :",now)
    print("\n")
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        print("\n")
        print("########################## for next_node in graph[now]: 시작 ########################")
        print(graph,"[",now,"] :",graph[now])
        print("next_node :",next_node)
        print("distance :",distance)
        print("\n")
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            print("\n")
            print("########################## if distance[next_node] == -1 시작 ########################")
            print(distance,"[",next_node,"] :",distance[next_node])
            print(distance,"[",now,"] :",distance[now])
            distance[next_node] = distance[now] + 1
            print("처리 이후",distance,"[",next_node,"] :",distance[next_node])
            print("q :",q)
            q.append(next_node)
            print("next_node :",next_node)
            print("처리 이후 q :",q) # (처음 방문 하는 노드에 한해서 q에 stack)
            print("\n")
# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print("i 값 산출",i)
        check = True
# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)
#1. 
# graph_c = [[] * 3] => [[]] 가 되므로 
# [[] for _ in range(N)] 가 정답답 
# print(graph_c)




