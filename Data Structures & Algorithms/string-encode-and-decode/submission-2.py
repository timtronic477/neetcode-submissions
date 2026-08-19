class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for i in strs:
            enc += "/?"+i
        return enc


    def decode(self, s: str) -> List[str]:
        return s.split("/?")[1:]
