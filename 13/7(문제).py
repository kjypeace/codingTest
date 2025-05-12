######################## 복습 때 마다, 풀어보는 칸 ##########################
# 입력예시
# 2 20 50 (NXN 크기의 땅) (두 나라의 인구 차이가 L명 이상, R명 이하)
# 50 30  둘째 줄 부터 N개의 줄에 각 
# 20 40 나라의 인구수가 주어짐
# 출력예시
# 1 (인구 이동 발생 횟수)

from collections import deque
n,l,r = 2,20,50
graph = []
data_list = [[50,30],[20,40]]
for data in data_list:
    graph.append(data)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def process(x,y,index):
    united = []
    united.append((x,y))
    q = deque()
    q.append((x,y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < n and union[nx][ny] == -1:
                if l <=abs(graph[nx][ny]-graph[x][y]) <= r:
                    q.append((nx,ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx,ny))
        for i,j in united:
            graph[i][j] = summary // count
total_count = 0
                 
while True:
    union = [[-1]*(n) for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j,index)
                index += 1
    if index == n*n:
        break
    total_count += 1


print(total_count)
#########################내가 풀어 본 코드################################