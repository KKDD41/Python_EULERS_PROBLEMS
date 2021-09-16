import math, sys
# хуячит следующую лексикографическую перестановку
def the_next_one(S: list):
    n = len(S) - 1
    i = 1
    prefix = [S[n]]
    S.pop()
    while i<n+1:
        if S[n-i]>=prefix[i-1]:
            prefix.append(S[n-i])
            S.pop()
            i+=1
        else:
            break
    if S == []:
        prefix.reverse()
        return prefix
    else:
        t = S[n-i]
        for k in range(len(prefix)):
            if t<prefix[k]:
                S.pop()
                S.append(prefix[k])
                prefix.remove(prefix[k])
                prefix.append(t)
                prefix.sort()
                S.extend(prefix)
                break
            else:
                pass
        return S

S = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(999999):
    S = the_next_one(S)

print(S)