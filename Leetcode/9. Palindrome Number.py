import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return  False
        return  x == self.rev(x)

    def rev(self,num):
        return int(num != 0) and ((num % 10) * \
                                  (10 ** int(math.log(num, 10))) + \
                                  self.rev(num // 10))

solution = Solution()

print(solution.isPalindrome(-123))