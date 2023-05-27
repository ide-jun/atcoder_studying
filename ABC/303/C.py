N, M, H, K = map(int, input().split())
S = input()
items = {}
for i in range(M):
    x, y = map(int, input().split())
    if x not in items.keys():
        items[x] = []
    items[x].append(y)
pos_x = 0
pos_y = 0
flag = True
for i in range(N):
    if S[i] == 'R':
        pos_x += 1
    elif S[i] == 'L':
        pos_x -= 1
    elif S[i] == 'U':
        pos_y += 1
    else:
        pos_y -= 1
    H -= 1
    if H < 0:
        flag = False
        break
    if pos_x in items.keys() and pos_y in items[pos_x] and H < K:
        H = K
        items[pos_x].remove(pos_y)
if flag:
    print("Yes")
else:
    print("No")
