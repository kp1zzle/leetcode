from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sortedWords = sorted(words, key=lambda s: len(s), reverse=True)
        map = {w: 1 for w in sortedWords}
        for index, word in enumerate(sortedWords):
            for i in range(len(word)):
                nextWord = word[:i] + word[i + 1:]
                if nextWord in map.keys():
                    map[nextWord] = max(map.get(nextWord), map.get(word) + 1)
        return max(map.values())


if __name__ == '__main__':
    sol = Solution()
    list = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
    result1 = sol.longestStrChain(["a","b","ba","bca","bda","bdca"])
    pass