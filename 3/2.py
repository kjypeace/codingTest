# N = 배열의 크기 / M = 숫자가 더해지는 횟수 / K번 초과해서 더해질 수는 없음.
# 5 8 3
# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

# 2 4 5 4 6 => 2 4 4 5 6
data.sort() # 입력 받은 수들 정렬하기 => data : [2, 4, 4, 5, 6]
print("data :",data)
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
print("count :", count)
count += m % (k + 1)
print("count :", count)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력
