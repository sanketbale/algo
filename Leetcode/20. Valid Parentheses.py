from typing import List

class Solution:
    def isValid(self, symbolString: str) -> bool:
        s = list()
        balanced = True
        index = 0
        while index < len(symbolString) and balanced == True:
            symbol = symbolString[index]
            if symbol in "([{":
                s.append(symbol)
            else:
                if len(s) == 0:
                    balanced = False
                else:
                    top = s.pop()
                    if not self.matches(top, symbol):
                        balanced = False
            index = index + 1

        if balanced and len(s) == 0:
            return True
        else:
            False

    def matches(self,open, close) -> bool:
        opens = "([{"
        closers = ")]}"
        return opens.index(open) == closers.index(close)

solution = Solution()
print(solution.isValid('()'))
