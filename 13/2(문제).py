######################## 복습 때 마다, 풀어보는 칸 ##########################
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

n, m = 3, 3
data = []
temp = [[0] * m for _ in range(n)]
map_list = [[2,0,1],[1,0,0],[0,0,0]]
for i in range(n):
    data.append(map_list[i])    
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0 :
                temp[nx][ny] = 2
                virus(nx,ny)
                   
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global  result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        result = max(result,get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1  
                dfs(count)
                data[i][j] = 0
                count -= 1
                

                
dfs(0)
print(result)