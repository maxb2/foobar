import math

def solution(x):
    xx = long(x)
    count = 0 
    if xx == 0:
        return 1

    while xx != 1:
        # print(count,xx)
        if xx % 2 == 0:
            count += 1
            xx = xx/2
        p = math.log(xx,2)
        a = 2**int(math.floor(p))
        b = 2**int(math.ceil(p))
        down = xx-a
        up = b-xx
        if up >= down:
            count += down
            xx -= down
        else:
            count += up
            xx += up
    return count