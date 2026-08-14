class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s1 = set(nums[0])

        for row in nums:
            s1 = s1.intersection(set(row))

        l1 = list(s1)
        l1.sort()

        return l1