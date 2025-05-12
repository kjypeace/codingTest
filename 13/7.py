#########################
import inspect

# print(f"현재 줄 번호: {inspect.currentframe().f_lineno}")
#########################
# 입력예시
# 2 20 50 (NXN 크기의 땅) (두 나라의 인구 차이가 L명+ 이상, R명 이하)
# 50 30  둘째 줄 부터 N개의 줄에 각 
# 20 40 나라의 인구수가 주어짐
# 출력예시
# 1 (인구 이동 발생 횟수)

from collections import deque

# 땅의 크기(N), L, R 값을 입력받기
# n, l, r = map(int, input().split())
n, l, r = 2, 20 ,50

# 전체 나라의 정보(N x N)를 입력 받기
graph = []
data_list = [[50,30],[20,40]]
# for _ in range(data_list):
#     graph.append(list(map(int, input().split())))
    
for data in data_list:
    graph.append(data)

print("graph :",graph)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    print("x :",x)
    print("y :",y)
    print("index :",index)
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    print("united :",united)
    print("x :",x)
    print("y :",y)
    
    # 너비 우선 탐색 (BFS)을 위한 큐 라이브러리 사용
    q = deque()
    print("q :",q)
    q.append((x, y))
    print("x :",x)
    print("y :",y)
    print("q :",q)
    # 현재 연합의 번호 할당
    union[x][y] = index 
    print("index :",index)
    print("union[x][y] :",union[x][y])
    print("x :",x)
    print("y :",y)
    # 현재 연합의 전체 인구 수
    summary = graph[x][y] 
    print("graph :",graph)
    print("x :",x)
    print("y :",y)
    print("summary :",summary)
    # 현재 연합의 국가 수
    count = 1 
    print("count :",count)
    # 큐가 빌 때까지 반복(BFS)
    while q:
        print("q :",q)
        x, y = q.popleft()
        print("x :",x)
        print("y :",y)
        print("q :",q)
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            print("i :",i)
            print("dx :",dx)
            print("dy :",dy)
            print("x :",x)
            print("y :",y)
            nx = x + dx[i]
            ny = y + dy[i]
            print("nx :",nx)
            print("ny :",ny)
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                print("graph :",graph)
                print("nx :",nx)
                print("ny :",ny)
                print("x :",x)
                print("y :",y)
                print("l :",l)
                print("r :",r)
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    print("q :",q)
                    q.append((nx, ny))
                    # print("q :",q)
                    # print("index :",index)
                    # print("union[nx][ny] :",union[nx][ny])
                    # print("union :",union)
                    # 연합에 추가하기
                    union[nx][ny] = index
                    # print("graph[nx][ny] :",graph[nx][ny])
                    # print("graph[x][y] :",graph[x][y])
                    # print("graph :",graph)
                    # 인구차이가 L과 R을 포함하는 내에서의 summary를 모두 더한 값
                    summary += graph[nx][ny] 
                    print("summary :",summary)
                    print("count :",count)
                    count += 1
                    # print("count :",count)
                    # print("nx :",nx)
                    # print("ny :",ny)
                    # print("united :",united)
                    united.append((nx, ny))
                    print("united :",united)
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        # print("united :",united)
        # print("i :",i)
        # print("j :",j)
        # print("graph :",graph)
        # print("graph[i][j] :",graph[i][j])
        # print("summary :",summary)
        # print("count :",count)
        graph[i][j] = summary // count
        print("graph[i][j] :",graph[i][j])

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    # index가 의미하는 바는? 인구이동을 처리했는지 여부를 나타내는 지표!
    # 만약 동일한 분배가 일어나는 국가라면 def process() 내에서
    # [if l <= abs(graph[nx][ny] - ~~~~ ] 에 의하여 동일한 index를 부여받게 됨 
    # (1차 분배에 한하여 2차분배는 다시 점검의 과정을 거침)
    index = 0
    # print("union :",union)
    # print("n :",n)
    # print("index :",index)
    for i in range(n):
        for j in range(n):
            # print("i :",i)
            # print("j :",j)
            # print("union[i][j] :",union[i][j])
            # 해당 나라가 아직 처리되지 않았다면
            if union[i][j] == -1: 
                # print("union[i][j] :",union[i][j])
                # print("i :",i)
                # print("j :",j)
                # print("index :",index)
                process(i, j, index)
                index += 1
                print("index :",index)
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    print("graph :",graph)
    print(total_count)
    # 아래의 total_count의 경우에는 이중 for문을 통해 i,j를 전부 다 돌아서 분배가 이뤄진 뒤에
    # 예를 들어
    # 50 20
    # 30 40
    # 에 대해서 주어진 조건하에 1차 분배가 이뤄지면
    # 35 35
    # 35 35
    # 가 되고 이후에 추가적으로 2차 분배가 이뤄지지 않을시
    # 즉 index 가 4가 될시에는 break를 통해 while문을 종료하게 된다! 
    # total_count가 +1 하게 된다.
    # 분배가 발생할 시 def process() 문 내의
    # union[nx][ny] = index 를 통해서 index 추가를 건너띄게 된다!
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)
