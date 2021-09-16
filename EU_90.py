from itertools import combinations


def extend(S):
    return S.union({9, 6}) if 6 in S or 9 in S else S


def achieve(pair, S1, S2):
    assert len(pair) == 2
    if (pair[0] in S1 and pair[1] in S2) or (pair[0] in S2 and pair[1] in S1):
        return True
    else:
        return False


set_of_pairs = [[0, 1], [0, 4], [0, 9], [1, 6], [2, 5], [3, 6], [4, 9], [6, 4], [8, 1]]
q = 0
for j in list(combinations(range(10), 6)):
    for i in list(combinations(range(10), 6)):
        s = 1
        for pair in set_of_pairs:
            if s == 0:
                break
            else:
                s = s*achieve(pair, extend(set(i)), extend(set(j)))
        if s == 1:
            print(i, j)
            q +=1
        else:
            pass

print('stop', q, q/2)
