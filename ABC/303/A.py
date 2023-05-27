N = int(input())
S = input()
T = input()
TF = True
for i in range(N):
    if S[i] == T[i]:
        continue
    elif S[i] == '1' and T[i] == 'l' or S[i] == 'l' and T[i] == '1':
        continue
    elif S[i] == '0' and T[i] == 'o' or S[i] == 'o' and T[i] == '0':
        continue
    else:
        TF = False
        break
if TF:
    print("Yes")
else:
    print("No")
