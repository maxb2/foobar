import solution

tests = [
    {"in": ([1, 2, 3, 4], 15), "out": [-1,-1]}, 
    {"in": ([4, 3, 10, 2, 8], 12), "out": [2,3]}, 
    {"in": ([4, 3, 10, 2, 8], 27), "out": [0,4]}, 
    {"in": ([4, 3, 4, 3], 7), "out": [0,1]}]


for test in tests:
    print(solution.solution(*test["in"]))
    print(test["out"] == solution.solution(*test["in"]))