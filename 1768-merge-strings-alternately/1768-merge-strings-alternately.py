class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ""
        i = 0
        j = 0 
        while i != len(word1) or j!= len(word2):
            if len(word1) > i:
                mergedString += word1[i]
                i += 1
            if len(word2) > j:
                mergedString += word2[j]
                j += 1
        return mergedString