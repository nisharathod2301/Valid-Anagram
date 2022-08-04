class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        #If the sorted strings of s and t are equal its an anagram 
