class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        counts = {}

        for i in s:
            counts[i] = counts.get(i, 0) + 1

        for j in t:
            if j in counts:
                counts[j] = counts.get(j, 0) - 1
        
        return all(v == 0 for v in counts.values())

        