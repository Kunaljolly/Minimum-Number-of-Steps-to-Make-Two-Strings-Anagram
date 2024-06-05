from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)
        counter_diff = counter_s - counter_t
        return sum(counter_diff.values())
