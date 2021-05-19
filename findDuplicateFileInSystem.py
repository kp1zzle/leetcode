import collections
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        map = collections.defaultdict(list)
        for path in paths:
            files = path.split(' ')
            directory_path = files[0]
            for file in files[1:]:
                file_name, content = file.strip(')').split('(')
                map[content].append(directory_path + '/' + file_name)
        return [x for x in map.values() if len(x) > 1]


if __name__ == '__main__':
    sol = Solution()
    result = sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"])
    print(result)
    result2 = sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"])
    print(result2)