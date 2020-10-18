# Solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {num : i for i, num in enumerate(nums)}
        for i1, n1 in enumerate(nums):
            if target - n1 in nums and m[target - n1] != i1:
                return sorted([i1, m[target - n1]])
            
        return None