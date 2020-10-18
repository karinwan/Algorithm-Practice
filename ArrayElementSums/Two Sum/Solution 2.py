# Solution 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i1, n1 in enumerate(nums):
            if target - n1 in m:
                return [m[target - n1], i1]
            m[n1] = i1
        return None