######################## 복습 때 마다, 풀어보는 칸 ##########################
#입력 예시
# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X
#출력 예시 (모든 학생들이 감시를 피할 수 있는지 없는지 여부에 해당)
# YES

from itertools import combinations
n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j)) 
        if board[i][j] == 'X':
            spaces.append((i,j))
            
def watch(x,y,direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False
            
def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
    return False

for data in combinations(spaces,3):
    for x,y in data:
        board[x][y] = 'O'
    if not process():
        find = True
        break
    for x,y in data:
        board[x][y] = 'X'

if find == True:
    print("Yes")
else:
    print("No")