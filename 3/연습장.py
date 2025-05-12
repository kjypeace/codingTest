n = int(7)
t = []
p = []
dp = [0] * (n+1)
max_value = 0

data_list = [[3,10],[5,20],[1,10],[1,20],[2,15],[4,40],[2,200]]

for i in range(n):
    x,y = data_list[i]
    t.append(x)
    p.append(y)
    
for i in range(n-1,-1,-1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
        
print(max_value)