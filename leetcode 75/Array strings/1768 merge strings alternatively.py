class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        for i in range(min(len(word1),len(word2))):
            result+=word1[i]+word2[i]
        if len(word1)==len(word2):
            return result
        elif len(word1) > len(word2):
            return result+word1[len(word2):]
        else:
            return result+word2[len(word1):]
