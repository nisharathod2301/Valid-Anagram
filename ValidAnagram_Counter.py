class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
#Counter is a sub-class that is used to count hashable objects. It implicitly creates a hash table of an iterable when invoked. 
