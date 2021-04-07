def solution(l, t):
    n =len(l)
    for i1 in range(n):
        total = 0
        for i2 in range(n-i1):
            total += l[i1+i2]
            if total > t:
                break
            elif total == t:
                return [i1,i1+i2]

    return [-1,-1]