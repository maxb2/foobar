import solution

tests = [
    {"in": ('4','7'), "out": "4"}, 
    {"in": ('2','1'), "out": "1"}, 
    {"in": ('2','4'), "out": "impossible"}]


for test in tests:
    print(test["in"])
    sol = solution.solution(*test["in"])
    print(sol)
    print(test["out"] == sol)