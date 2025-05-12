from collections import deque

n,k = 3,3
graph = []
data = []
copymap = [[1,0,2],[0,0,2],[3,0,0]]
for i in range(n):
    graph.append(copymap[i])
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j))
            
            
data.sort()
q = deque(data)

target_s,target_x,target_y = 2, 3, 2

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
    virus,s,x,y = q.popleft()
    
    if s == target_s:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus,s+1,nx,ny))

print(graph[target_x - 1][target_y - 1])