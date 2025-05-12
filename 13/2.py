# BOJ에서는 [언어]를 PyPy3로 설정하여 제출해주세요.
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
# 이해를 위해 바꾼 아주 쉬운 입력
# 3 3
# 2 0 1
# 1 0 0
# 0 0 0
# n, m = map(int, input().split())
n, m = 3,3
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트
map_list = [[2,0,1],[1,0,0],[0,0,0]]

# for _ in range(n):
#     data.append(list(map(int, input().split())))

for i in range(n):
    data.append(map_list[i])

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매 번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        print("data :",data)
        print("temp :",temp) #temp는 바이러스 확장을 검사하기 위한 맵 data를 복사함
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최대값 계산
        # 위 코드를 통해 virus는 다 퍼진 경우
        result = max(result, get_score())
        return
    # 빈 공간에 울타리를 설치
    # 이 부분이 어려운데 차근차근 설명해 보겠음
    # 맵이 
    # 2 0 1
    # 1 0 0
    # 0 0 0
    # 이라고 하자 
    # 2중 for문을 통해서 
    # 2 1 1
    # 1 0 0
    # 0 0 0 
    # 을 만들고 카운트 +1 함
    
    # 그다음 다시 2중 for문 돌면서
    # 2 1 1
    # 1 1 0
    # 0 0 0 
    # 을 만들고 카운트 +1 함
    
    # 다시 또 2중 for문 돌면서
    # 2 1 1
    # 1 1 1
    # 0 0 0
    # 을 생성하면서 카운트 +1 함 ( 이 시점에서 카운트는 3)
    # 여기서 중요한게 2중 for문 안의 if문 내의 dfs에 들어가서
    # score와 result를 반환하면서 dfs(count)를 끝냄
    
    # 그 다음 
    # data[i][j] = 0
    # count -= 1
    # 을 통하여 카운트를 3 -> 2로 바꾸고
    
    # 2 1 1
    # 1 1 0
    # 0 0 0
    
    # 으로 바꿈 그 다음 다시
    # 카운트 2인 상태에서 for문을 돌며
    
    # 2 1 1
    # 1 1 0
    # 1 0 0
    
    # 이런식으로 하나씩 검증하고 result와 score를 계산하는 방식
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                # 전체적인 순서는 아래와 같다.
                # 기존맵이 있음
                # 기존맵에서 임의로 안전울타리를 3개침
                # 울타리친 맵안에서 바이러스가 퍼짐
                # 이를 통해 안전영역을 계산함
                # 아래의 과정을 통해 안전울타리를 제거함
                # 이것을 모든 안전울타리 경우의 수에대하여 진행행
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)


#1.
# N,M = map(int,input().split())
# graph = []
# for i in range(N):
#     row = list(map(int, input().split()))[:M]  # 입력을 리스트로 변환 후 M개까지만 유지
#     graph.append(row)  # 리스트 추가
# print(graph)