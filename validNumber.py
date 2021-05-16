def strGet(s: str, i: int):
    if i < 0:
        return None
    try:
        return s[i]
    except Exception as e:
        return None


class Solution:
    def isNumber(self, s: str) -> bool:
        shouldAcceptDecimalPoint = True
        shouldAcceptPosOrNegSign = True
        shouldAcceptE = False
        haveSeenE = False
        for index, c in enumerate(s):
            if c == '.':
                if shouldAcceptDecimalPoint and \
                        (strGet(s, index+1) or strGet(s, index-1) not in ['+', '-', None]):
                    shouldAcceptDecimalPoint = False
                    shouldAcceptPosOrNegSign = False
                else:
                    return False
            elif c == '-' or c == '+':
                if shouldAcceptPosOrNegSign and strGet(s, index+1):
                    shouldAcceptPosOrNegSign = False
                else:
                    return False
            elif c == 'e' or c == 'E':
                if shouldAcceptE and strGet(s, index+1):
                    haveSeenE = True
                    shouldAcceptE = False
                    shouldAcceptDecimalPoint = False  # since number after e must be int
                    shouldAcceptPosOrNegSign = True  # pos/neg sign scope resets
                else:
                    return False
            elif c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return False
            else:
                # c is a digit
                shouldAcceptPosOrNegSign = False
                shouldAcceptE = not haveSeenE

        return True


if __name__ == "__main__":
    sol = Solution()
    for testCase in ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]:
        result = sol.isNumber(testCase)
        assert result is True

    for testCase in ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", '.', '+', '-']:
        result = sol.isNumber(testCase)
        assert result is False