# 1. 바이러스는 번호가 낮은 순서대로 차례대로
# 증식 1번 (상 하 좌 우) 증식 -> 2번 (상 하 좌 우) 증식
# 이런 식
# 2. S초가 지난 후에 (X,Y)에 존재하는 바이러스 종류를 출력하는 프로그램 작성
# 입력 예시
# N 과 K 이면 N개의 줄에 걸쳐 맵이 입력됨
# 모든 바이러스 번호는 K 이하의 자연수
# 3 3 
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2 (s초 x,y)
# 출력은 3 (출력값은 s초 뒤에 x,y 좌표에 있는 바이러스 종류를 출력하는 것!)

from collections import deque

# n, k = map(int, input().split())
n, k = 3,3
graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트
copymap = [[1,0,2],[0,0,2],[3,0,0]]
for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    # graph.append(list(map(int, input().split())))
    graph.append(copymap[i])
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

print("17 graph :",graph)
# 바이러스 종류와 시간 그리고 좌표를 0초 기준으로 data 2차원 리스트로 저장한 그래프
print("18 data :",data) 
# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)
 
print("23 data :",data) 
print("24 q :",q)

print("S, X , Y 를 입력하세요(S초가 지난 후에 (X,Y)에 존재하는 바이러스 종류를 출력)")
# target_s, target_x, target_y = map(int, input().split())
target_s, target_x, target_y = 2, 3, 2
 
# 바이러스가 퍼져나갈 수 있는 4가지의 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    print("37 q :",q)
    print("38 virus, s, x, y :",virus, s, x, y)
    print("39 s :",s)
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            print("49 if문 실행이 가능함에 따라 바이러스 넣기")
            print("50 graph[",nx,"][",ny,"] :",graph[nx][ny])
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))
# 위의 q 에 추가되는값은 virus( 몇 번 바이러스) 가 (s+1) 초에 (nx,ny) 위치에 퍼졌다! 를 의미미
print("50 target_x :",target_x)
print("51 target_y :",target_y)
print("53 graph :",graph)




print(graph[target_x - 1][target_y - 1])
