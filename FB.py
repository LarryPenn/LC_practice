#https://leetcode.com/problems/verifying-an-alien-dictionary


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        def loc(char, order):
            for i in range(len(order)):
                if char == order[i]:
                    return i
            
            return -1
        
        def comp(word1, word2, order):
            
            for i in range(min(len(word1), len(word2))):
                if loc(word1[i], order) < loc(word2[i], order):
                    return True
                elif loc(word1[i], order) > loc(word2[i], order):
                    return False
                else: 
                    continue
            
            if len(word1) > len(word2):
                return False
            
            return True
        
        for i in range(len(words)-1):
            if not comp(words[i], words[i+1], order):
                return False
            
        return True
            