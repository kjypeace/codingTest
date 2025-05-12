#########################
# import inspect

# print(f"현재 줄 번호: {inspect.currentframe().f_lineno}")
#########################
# 입력 예시
# 2
# 5 6
# 0 0 1 0

# 출력 예시
# 30
# 30

# 입력 예시
# 3
# 4 5 6
# 0 0 2 0

# n = int(input())
n = int(3)
# 연산을 수행하고자 하는 수 리스트
# data = list(map(int, input().split()))
data = list([4,5,6])
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
# add, sub, mul, div = map(int, input().split())
add, sub, mul, div = 2,0,2,0

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색 (DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
            print("add:",add)
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
            print("sub :",sub)
        if mul > 0:
            print("mul :",mul)
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
            print("mul :",mul)
        if div > 0:
            print("div :",div)
            div -= 1
            dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
            div += 1
            print("div :",div)

# DFS 메서드 호출
dfs(1, data[0])
# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)
