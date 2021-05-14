from typing import List


def computePossibleCoords(s: str) -> List[str]:
    if len(s) == 1:
        return [s]

    returnList = []
    if s[0] != '0':
        returnList.append(s)
    for decimalIndex in range(1, len(s)):
        beforeDecimal = s[:decimalIndex]
        afterDecimal = s[decimalIndex:]
        if (len(beforeDecimal) == 1 or beforeDecimal[0] != '0') and afterDecimal[-1] != '0':
            returnList.append("{}.{}".format(beforeDecimal, afterDecimal))
    return returnList


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        outputList = []
        for splitIndex in range(2, len(s)-1):
            left = s[1:splitIndex]
            right = s[splitIndex:-1]

            leftPossibles = computePossibleCoords(left)
            rightPossibles = computePossibleCoords(right)

            for leftNum in leftPossibles:
                for rightNum in rightPossibles:
                    outputList.append('({}, {})'.format(leftNum, rightNum))
        return outputList
