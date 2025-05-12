# 본 코드의 주석은 2 2 / 1 1 4 4 기준으로 작성 
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    # print(data) => 한 줄 입력 할때마다 [1, 1] / [4, 4] 이런식으로 출력 
    for a in data:
        # print(a) => 1 1 4 4 
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력