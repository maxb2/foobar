
import solution

tests = [
    {"in": "wrw blf hvv ozhg mrtsg'h vkrhlwv?", "out": "did you see last night's episode?"}, 
    {"in": "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!", "out": "Yeah! I can't believe Lance lost his job at the colony!!"}]


for test in tests:
    print(solution.solution(test["in"]))
    print(test["out"] == solution.solution(test["in"]))