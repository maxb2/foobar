# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -ExecuteTime,-execute,-execution
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
Gearing Up for Destruction 
==========================

As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple - just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.


# %%
def solution(pegs):
    peg_num = len(pegs)
    if 2 > peg_num or peg_num > 20:
        return "wrong number of pegs"
    sorted_pegs = sorted(pegs)
    if pegs != sorted_pegs:
        return "Please provide peg positions in ascending order"
    last_gear = 0
    peg_sign = -1
    even_max = -11111.0
    odd_min = 11111.0
    for i in range(peg_num-1):
        if i==0:
            if 1 > pegs[i] or pegs[i] > 10000:
                return "At least one peg won't fit on the beam!"
        if 1 > pegs[i+1] or pegs[i+1] > 10000:
            return "At least one peg won't fit on the beam!"
        inner_peg_dist = pegs[i+1]-pegs[i]
        last_gear -= peg_sign*inner_peg_dist
        peg_sign *= -1
        if i % 2 == 0:
            odd_min = min(odd_min, last_gear)
        else:
            even_max = max(even_max, last_gear)
    numerator_r0 = 2*last_gear
    denominator_r0 = abs(1+2*peg_sign)
    if numerator_r0 < denominator_r0*(even_max +1) or numerator_r0 > denominator_r0 * (odd_min - 1):
        return [-1,-1]
    if peg_sign == 1 and numerator_r0 % 3 == 0:
        numerator_r0 = int(numerator_r0/3)
        denominator_r0 = 1
    return [numerator_r0,denominator_r0]
t0 = [2,30,50, 60]
t1 = [4, 30, 50]
t2 = [4,18,50]
t3 = [30,2,50]
t4 = [4, 30, 50, 70, 100, 130, 150, 170, 195, 220]
print(solution(t1))

# %%
