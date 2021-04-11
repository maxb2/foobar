
import solution

tests = [
    {"in": ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"], "out": ["0.1","1.1.1","1.2","1.2.1","1.11","2","2.0","2.0.0"]}, 
    {"in": ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], "out": ["1.0","1.0.2","1.0.12","1.1.2","1.3.3"]}]


for test in tests:
    print(test["in"])
    print(solution.solution(test["in"]))
    print(test["out"] == solution.solution(test["in"]))