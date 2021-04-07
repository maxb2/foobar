
import solution

tests = [
    {"in": "4", "out": 2}, 
    {"in": "15", "out": 5}]


for test in tests:
    sol = solution.solution(test["in"])
    print(sol)
    print(test["out"] == sol)