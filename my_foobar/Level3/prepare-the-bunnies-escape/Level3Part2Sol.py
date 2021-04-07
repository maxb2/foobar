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
#     display_name: Python [conda env:.conda-ds-OnboardingHurstT]
#     language: python
#     name: conda-env-.conda-ds-OnboardingHurstT-py
# ---

# %%
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
    7

Input:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
Output:
    11

-- Java cases --
Input:
Solution.solution({{0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0}})
Output:
    7

Input:
Solution.solution({{0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0}})
Output:
    11

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.


# %%
#Initial working solution
def solution(map):
    w, h = len(map[0]), len(map) #Width and height
    shortest_path = 401
    for a_map in all_maps(map):
#        Find min path length
        shortest_path = min(min_path(a_map, w, h), shortest_path)
        if shortest_path == w + h - 1:
            return shortest_path
    return shortest_path
def min_path(map, w, h):
    d = {1: {(0,0)}}
    short_path = 2
    while short_path < 401 and d[short_path-1]:
        explored = set()
        for x in d[short_path-1]:
            unexplored_x = {y for y in open_neighbors(x, map) if not any(y in visited for visited in d.values())}
            explored = explored | unexplored_x
        if (h-1, w-1) in explored:
            return short_path
        d[short_path] = explored
        short_path += 1
        
    return 401
def open_neighbors(x,map):
    i, j = x
    w, h = len(map[0]), len(map)
    adjacent_spaces = {(i-1, j), (i+1, j), (i, j-1), (i, j+1)}
    open_neighbors = set()
    for y in adjacent_spaces:
        k, l = y
        if k >= 0. and k<h and l>=0 and l<w and map[k][l] == 0:
            open_neighbors.add(y)
    return open_neighbors
def all_maps(map):
    yield map
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j]:
                copy = [[col for col in row] for row in map]
                copy[i][j] = 0
                yield copy

    
t0 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
t1 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(solution(t0))
print(solution(t1))


# %%
#Final submitted solution
def solution(map):
    w, h = len(map[0]), len(map) # Map width and height
    shortest_path = 401 # Initialize at impossibly large path length 
    all_maps = [map] # Removing a wall may not help
    short_path_list =[401]
    # Generate all the maps with one wall removed
    for i in range(h):
        for j in range(len(map[i])):
            if map[i][j]==1:
                copy = [[col for col in row] for row in map]
                copy[i][j] = 0
                all_maps.append(copy)
    # Find the minimum path length for each map 
    # and compare that to the shortest discovered path
    for a_map in all_maps:
#        Find min path length
        d = {1: {(0,0)}}
        short_path = 2 # Initialize counter with first and ending nodes included
        count = 0
        while short_path < 401 and d[short_path-1]:
            explored = set()
            for x in d[short_path-1]:
                i, j = x
                adjacent_spaces = {(i-1, j), (i+1, j), (i, j-1), (i, j+1)}
                open_neighbors = set()
                for space in adjacent_spaces:
                    k, l = space
                    if k >= 0. and k<h and l>=0 and l<w and a_map[k][l] == 0:
                        open_neighbors.add(space)
                unexplored_x = {y for y in open_neighbors if not any(y in visited for visited in d.values())}
                explored = explored | unexplored_x
            
            if (h-1, w-1) in explored: # Did we reach an escape pod?
                shortest_path = min(short_path, shortest_path)
                count +=1
            d[short_path] = explored
            short_path += 1
        if count == 0:
            shortest_path = min(shortest_path, 401) 
        if shortest_path == w + h - 1:
            return shortest_path
    return shortest_path


    
t0 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
t1 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(solution(t0))
print(solution(t1))
