

class Solution : 
    def isAnagram1(self , s , t ):

        if len(s) != len(t) :
            return False
        count1 = [0 for _ in range(26)]
        count2 = [0 for _ in range(26)]
        for i in range(len(s)):
            count1[ord(s[i]) - ord('a')] += 1 
            count2[ord(t[i]) - ord('a')] += 1 
        return count1 == count2


    def isAnagram(self , s , t ):

        if len(s) != len(t) :
            return False
        count = [0 for _ in range(26)]
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 
            count[ord(t[i]) - ord('a')] -= 1 
        for val in count:
            if val != 0 :
                return False
        return True


