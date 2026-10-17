class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0  # Our current position in the encoded string
    
        while i < len(s):
        # 1. Find where the next '#' is, starting from index i
            delim_idx = s.find('#', i)
        
        # 2. Everything between our current position and '#' is the length
            length = int(s[i:delim_idx])
        
        # 3. Slice out the word right after '#' using our length
            word = s[delim_idx + 1 : delim_idx + 1 + length]
            res.append(word)
        
        # 4. Jump our pointer completely past the word we just extracted
            i = delim_idx + 1 + length
        
        return res
