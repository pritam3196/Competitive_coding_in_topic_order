"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Solution:
1st method: we can use hashmaps for both the strings. The time and space complexity would be 
O(s+t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	#return Counter(s) == Counter(t) - won't work in interviews
    	#return sorted(s) == sorted(t) - method 2

    	if len(s) != len(t):
    		return False

    	countS, countT = {}, {}

    	for i in range(len(s)):
    		countS[s[i]] = 1 + countS.get(s[i], 0)
    		countT[t[i]] = 1 + countT.get(t[i], 0)

    	for c in countS:
    		if countS[c] != countT.get(c,0):
    			return False

    	return True


"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	if len(s) != len(t):
    		return False

    	countS, countT = {}, {}

    	for i in range(len(s)):
    		countS[s[i]] = 1 + countS.get(s[i], 0)
    		countT[t[i]] = 1 + countT.get(t[i], 0)

    	for c in countS:
    		if countS[c] != countT.get(c,0):
    			return False

    	return True