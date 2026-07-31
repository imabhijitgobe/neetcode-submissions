class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map appraoch
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                if i > seen[need]:
                    return [seen[need], i]
                else :
                    return [i, seen[need]]
            seen[num] = i
        return []