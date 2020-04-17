from typing import List


class Solution:
    def checkPossibility(nums: List[int]) -> bool:
        res = 0
        for i in range(0, len(nums)-2):
            if nums[i] < nums[i+1]:
                if res < 1:
                    return True
                if nums[i+1] < nums[i+2]:
                     res = res + 1
        return False


print(Solution.checkPossibility([4,2,3]))