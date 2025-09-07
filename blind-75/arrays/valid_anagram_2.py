# 8th August 2025
# blind 75 Arrays --> question no. 242 (2)
# leetcode-link --> https://leetcode.com/problems/valid-anagram/description/

# Main Concept : maintain frequency of each character with dict and then compare them.

# Intuition: Create two hashmaps and add each char in the map.
# Intuition: Now compare both the hashmaps 



class Solution:
    def isAnagram(self , first:str , second:str) -> bool:


        if len(first) != len(second):
            return False

        dict1 = {}
        dict2 = {}

        for i in range(len(first)):
            dict1[first[i]] = dict1.get(first[i],0) + 1 
            dict2[second[i]] = dict2.get(second[i],0) + 1 
        
        if dict1 == dict2 :
            return True
        
        return False








