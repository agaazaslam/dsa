from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for string in strs:
            array = [0 for _ in range(26)]
            for ch in string:
                array[ord(ch) - ord('a')] += 1
            dict[tuple(array)].append(string)

        return list(dict)


        
