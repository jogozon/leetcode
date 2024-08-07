class Solution:

    # put a delimiter in front of each string as well as the number of characters
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # start of the string
            i = j + 1
            # end of the string
            j = i + length
            res.append(s[i:j])
            # put index to the encoded part of the next string
            i = j
        return res
