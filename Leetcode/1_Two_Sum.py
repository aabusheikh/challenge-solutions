class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0, len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            rem = target - nums[i]
            if rem in d and d[rem] != i:
                return [d[rem], i]