X, Y, Z = map(int, input().split())
S = input()
dp = [[0 for i in range(len(S))] for j in range(2)]
if S[0] == 'a':
    dp[0][0] = X
    dp[1][0] = Y+Z
else:
    dp[0][0] = Y
    dp[1][0] = Z+X
for i in range(1, len(S)):
    if S[i] == 'a':
        dp[0][i] = min(dp[0][i-1]+X, dp[1][i-1]+(Z+X))
        dp[1][i] = min(dp[0][i-1]+(Y+Z), dp[1][i-1]+Y)
    else:
        dp[0][i] = min(dp[0][i-1]+Y, dp[1][i-1]+(Z+Y))
        dp[1][i] = min(dp[0][i-1]+(Z+X), dp[1][i-1]+X)
print(min(dp[0][-1], dp[1][-1]))
