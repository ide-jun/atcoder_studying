N, M = map(int, input().split())
a = [list(map(int, input().split())) for j in range(M)]
ans = [[True for i in range(N)] for j in range(N)]
for i in range(N):
    ans[i][i] = False
for i in range(M):
    for j in range(N-1):
        ans[a[i][j]-1][a[i][j+1]-1] = False
        ans[a[i][j+1]-1][a[i][j]-1] = False
out = 0
for i in range(N):
    for j in range(N):
        if ans[i][j]:
            out += 1
            ans[i][j] = False
            ans[j][i] = False
print(out)
