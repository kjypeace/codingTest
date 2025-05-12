#########################
import inspect

# print(f"현재 줄 번호: {inspect.currentframe().f_lineno}")
#########################
# 입력
# [[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]
# 출력
# 7
# 맵의 가장 왼쪽 상단이 (1,1)
# 0은 빈칸 1은 벽


# 쉬운입력
# [[0,0,1,1],[0,0,0,0],[1,1,0,0],[0,0,0,0]]
# 출력
# 
# 맵의 가장 왼쪽 상단이 (1,1)
# 0은 빈칸 1은 벽


from collections import deque
# 순서3.
def get_next_pos(pos, board):
    print("pos :",pos)
    # 아래의 borad는 외벽을 적용한 board =new_board
    print("board :",board)
    next_pos = [] # 반환 결과 (이동 가능한 위치들)
    pos = list(pos) # 현재 위치 정보를 리스트로 변환 (집합 → 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # print("pos1_x :",pos1_x)
    # print("pos1_y :",pos1_y)
    # print("pos2_x :",pos2_x)
    # print("pos2_y :",pos2_y)
    # (서 동 남 북)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 로봇 이동에대해서 추가적인 설명 : 현재 위치에서 [서 동 남 북]으로 이동하는 모든 경우를 계산한다
    # 거기다가 플러스 [서 동 남 북] 으로 이동한 뒤에, 입력받은 pos에 대하여
    # 회전할 수 있는 모든 경우의 수 + 움직일 수 있는 모든 경우의 수수를 next_pos에 추가한다 
    for i in range(4):
        # print("i :",i)
        # print("dx[i] :",dx[i])
        # print("dy[i] :",dy[i])
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            # print("pos1_next_x :",pos1_next_x)
            # print("pos1_next_y :",pos1_next_y)
            # print("pos2_next_x :",pos2_next_x)
            # print("pos2_next_y :",pos2_next_y)
            # print("next_pos :",next_pos)
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
            print("next_pos :",next_pos)
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        print("pos2_x :",pos2_x)
        print("pos1_x :",pos1_x)
        for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
            print("i :",i)
             # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                # print("pos1_x + i :",pos1_x + i)
                # print("pos1_y :",pos1_y)
                # print("board[pos1_x + i][pos1_y] :",board[pos1_x + i][pos1_y])
                # print("pos2_x + i :",pos2_x + i)
                # print("pos2_y :",pos2_y)
                # print("board[pos2_x + i][pos2_y] :",board[pos2_x + i][pos2_y])
                # print("next_pos :",next_pos)
                # 가로로 변하면 y가 변한다는 사실을 잊지 말 것 /
                # 세로로 변할시에 x가 변함함
                # 로봇의 왼쪽을 기준으로 오른쪽 프레임을 위 또는 아래로 회전
                # (2,1)(2,2) 로 로봇이 잡고있는 상황에대해서, (2,1)(3,1)이 된다고 생각하면 편함
                # ㅡ 가 왼쪽 값은 안변하고, ㅣ 로 된다 생각할 것
                # (가로일때 기준)
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                # 로봇의 오른쪽을 기준으롤 왼쪽 프레임의의 위 또는 아래로 회전
                # (가로일때 기준)
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
                # print("next_pos append 실행 직접 표에 그려보면 이해 쉬움")
                # print("중요한건 x,y 가 1,1 인 상황에서 오른쪽으로 이동하면 1,2가 된다는 것을 기억할 것")
                # print("next_pos :",next_pos)
                
    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        # print("pos2_y :",pos2_y)
        # print("pos1_y :",pos1_y)
        # 왼쪽으로 회전하거나, 오른쪽으로 회전
        for i in [-1, 1]: 
            # 로봇 왼쪽몸통 그리고 오른쪽몸통 기준으로 왼쪽 몸통 위의 칸이 비어있거나 또는 오른쪽 몸통 위의 칸이 비어있을때
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0: 
                # print("pos1_x :",pos1_x)
                # print("pos1_y + i :",pos1_y + i)
                # print("board[pos1_x][pos1_y + i] :",board[pos1_x][pos1_y + i])
                # print("pos2_x :",pos2_x)
                # print("pos2_y + i :",pos2_y + i)
                # print("board[pos2_x][pos2_y + i] :",board[pos2_x][pos2_y + i])
                # print("next_pos :",next_pos)
                # (세로일때 기준) 로봇의 아래쪽을 기준으로, 위쪽 프레임을 오른쪽 또는 왼쪽으로 회전
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                # (세로일때 기준) 로봇의 위쪽을 기준으로, 아래쪽 프레임을 오른쪽 또는 왼쪽으로 회전
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
                print("처리이후 next_pos :",next_pos)
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos


# 순서2.
def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    # 예를 들어
    # 00
    # 00
    # 이 맵이면 외곽에 벽을 두르면
    # 1111
    # 1001
    # 1001
    # 1111
    # 이 된다.
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    # print("n :",n)
    # print("board :",board)
    for i in range(n):
        for j in range(n):
            # print("i :",i)
            # print("j :",j)
            # print("board :",board)
            # print("board[i][j] :",board[i][j])
            # print("new_board :",new_board)
            # print("new_board[i + 1][j + 1] :",new_board[i + 1][j + 1])
            new_board[i + 1][j + 1] = board[i][j]
            # print("new_board :",new_board)
            # print("i+1 :",i+1)
            # print("j+1 :",j+1)
            # print("new_board[i + 1][j + 1] :",new_board[i + 1][j + 1])
    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)} # 시작 위치 설정
    q.append((pos, 0)) # 큐에 삽입한 뒤에
    visited.append(pos) # 방문 처리
    # print("pos :",pos)
    # print("q :",q)
    # print("visited :",visited)
    # 큐가 빌 때까지 반복
    while q:
        print("q :",q)
        pos, cost = q.popleft()
        # print("pos :",pos)
        # print("cost :",cost)
        # print("q :",q)
        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos:
            # print("pos :",pos)
            # print("n,n :",n,n)
            # print("cost :",cost)
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # print("pos :",pos)
            # print("new_board :",new_board)
            # print("next_pos :",next_pos)
            # print("visited :",visited)
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                # print("visited :",visited)
                # print("next_pos :",next_pos)
                # print("cost + 1 :",cost + 1)
                # print("q :",q)
                q.append((next_pos, cost + 1))
                # next_pos 자체가 소괄호로 묶여져 있어 굳이 한번더 
                # append할때 쓸 필요는 없음음
                visited.append(next_pos)
                # print("visited :",visited)
                # print("q :",q)
    return 0
# 순서1.
print(solution([[0,0,1,1],[0,0,0,0],[1,1,0,0],[0,0,0,0]]))