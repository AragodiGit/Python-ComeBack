"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false"""
import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)

        if c1 == c2:
            return True
        else:
            return False
        
        """Solution 2
        len_lst = []
        for j in range(max(len(t),len(s))):
            if len(t)>len(s):
                for i in t:
                    if s.count(i) != t.count(i):
                        return False
                else:
                    return True
            else:
                for i in s:
                    if s.count(i) != t.count(i):
                        return False
                else:
                    return True"""