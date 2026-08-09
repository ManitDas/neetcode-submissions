class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"
        return result 

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            hash = s.find("#", i)
            length = int(s[i : hash])
            string = s[hash + 1 : hash + 1 + length]
            result.append(string)
            i = hash + length + 1
        return result
