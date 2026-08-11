class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        window_count = {}
        for char in s2[0 : len(s1)]:
            window_count[char] = window_count.get(char, 0) + 1

        if window_count == s1_count:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            char_entering = s2[i + len(s1) - 1]
            char_leaving = s2[i - 1]

            window_count[char_entering] = window_count.get(char_entering, 0) + 1

            window_count[char_leaving] -= 1
            if window_count[char_leaving] == 0:
                del window_count[char_leaving]

            if window_count == s1_count:
                return True

        return False