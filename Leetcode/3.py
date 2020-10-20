from typing import List

class Solution:
    def longestValidParentheses(self, symbolString: str) -> int:
        s = list()
        balanced = True
        result = 0
        counter = 0
        index = 0
        while index < len(symbolString):
            symbol = symbolString[index]
            if symbol == "(":
                s.append(symbol)
            else:
                if len(s) == 0:
                    result = max(result,counter)
                    counter = 0
                else:
                    s.pop()
                    counter = counter + 1
            index = index + 1

        result = max(result, counter)
        print (s)
        print (counter)
        return result

solution = Solution()

print(solution.longestValidParentheses('()()()(()()'))
