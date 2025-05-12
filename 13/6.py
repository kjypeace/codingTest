

#입력 예시
# 5
# X S X X T
# T X S X X
# X X X X x
# X T X X Ｘ
# X X T X X
#출력 예시 (모든 학생들이 감시를 피할 수 있는지 없는지 여부에 해당)
# YES

# 아주 쉬운 입력 예시
# 3
# S X X
# X X X 
# T X X
#출력 예시 (모든 학생들이 감시를 피할 수 있는지 없는지 여부에 해당)
# YES

from itertools import combinations

# 복도의 크기
n = int(input()) 
# 복도 정보 (N x N)
board = [] 
# 모든 선생님 위치 정보
teachers = []
# 모든 빈 공간 위치 정보 
spaces = [] 

for i in range(n):
    board.append(list(input().split()))
    print("board :",board)
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        print("############### for j in range(n) 문 시작 ###############################")
        print("n :",n)
        print("i :",i)
        print("j :",j)
        print("board :",board)
        print("board[i][j] :",board[i][j])
        if board[i][j] == 'T':
            print("############### if board[i][j] == 'T' 문 시작 ###############################")
            print("board[i][j] :",board[i][j])
            print("i :",i)
            print("j :",j)
            teachers.append((i, j))
            print("teachers :",teachers)
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            print("############### if board[i][j] == 'X': 문 시작 ###############################")
            print("board[i][j] :",board[i][j])
            print("i,j :",i,j)
            print("spaces :",spaces)
            spaces.append((i, j))
            print("spaces :",spaces)

# 특정 방향으로 감시를 진행 (학생 발견: True, 학생 미발견: False)
def watch(x, y, direction):
    print("############### def watch(x, y, direction) 문 시작 ###############################")
    print("x, y, direction :",x, y, direction)
    print("direction :",direction)
    # 왼쪽 방향으로 감시
    if direction == 0:
        print("############### if direction == 0: ###############################")
        print("y :",y)
        # 맨 왼쪽 맨 위가 0,0 이고, 맨 왼쪽 맨 아래가 2,0 임 아래로 내려갈수록 + 1
        # 오른쪽으로 갈 수록 + 1/ y >= 0 이 뜻하는 바는 오른쪽으로 갈 수 있는 상황이기에 오른쪽으로 못갈때 까지 -1 하겠다는 뜻
        while y >= 0:
            print("############### while y >= 0: ###############################")
            print("x,y :",x,y)
            print("board[x][y] :",board[x][y])
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y -= 1
            print("y :",y)
    # 오른쪽 방향으로 감시
    if direction == 1:
        print("############### if direction == 1: ###############################")
        print("direction :",direction)
        # y(오른쪽)으로 갈 수 있는데 까지 가기 
        while y < n:
            print("############### while y < n ###############################")
            print("y :",y)
            print("n :",n)
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y += 1
    # 위쪽 방향으로 감시
    # data = [(1,2)(3,4)] 에 대해서  data[0] 은 (1,2) data[1] 은 (3,4)
    # data[0][0] 은 1을 data[0][1] 은 2를 의미 즉  x,y 라고 했을때
    # x값의 변화는 x-y 좌표에대한 y값의 변화
    # y값의 변화는 x-y 좌표에대한 x값의 변화를 의미! 
    if direction == 2:
        print("############### if direction == 2: ###############################")
        print("direction :",direction)
        while x >= 0:
            print("############### while x >= 0 ###############################")
            print("x :",x)
            print("board[x][y] :",board[x][y])
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 3:
        print("############### if direction == 3: ###############################")
        print("direction :",direction)
        while x < n:
            print("############### while x < n: ###############################")
            print("x :",x)
            print("n :",n)
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생의 위치를 하나씩 확인
    print("board :", board)
    print("teachers :",teachers)
    for x, y in teachers:
        print("x :",x)
        print("y :",y)
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            print("i :",i)
            if watch(x, y, i):
                # watch가 True가 된다는 것은, 한마디로 선생이 학생을
                # 바로 눈앞에 볼 수 있는 상황이라는 뜻뜻
                print("watch(x, y, i)가 true")
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    print("data :",data)
    # 장애물들을 설치해보기
    for x, y in data:
        print("x :",x)
        print("y :",y)
        print("data :",data)
        board[x][y] = 'O'
        print("board[x][y] :",board[x][y])
    # 학생이 한 명도 감지되지 않는 경우
    # 아래의 process() 가 False가 될 경우 not False가 됨에 따라 True 가 되어 실행됨!!
    if not process():
        # 원하는 경우를 발견한 것임
        # 생각해야하는게 이 코드의 목적은 선생이 학생을 발견하지 않는 것!
        # 이 주 목표임 따라서 process 내의 watch문이 전부 False가 되어 최종적으로
        # False를 반환한다면 find는 True가 되어 YES가 프린트 됨
        print("####################### process가 False가 되어 결국에는 find = True ##################")
        find = True
        break
    # 설치된 장애물을 다시 없애기
    
    for x, y in data:
        print("x :",x)
        print("y :",y)
        print("data :",data)
        print("board[x][y] :",board[x][y])
        board[x][y] = 'X'
        print("board[x][y] :",board[x][y])

if find == True:
    print('YES')
else:
    print('NO')
