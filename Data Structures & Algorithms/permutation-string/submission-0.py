class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        #Step 1: Initialize s1 hashmap and map all frequencies
        s1_map = {}
        for i in s1:
            if i not in s1_map:
                s1_map[i] = 1
            else:
                s1_map[i] += 1

        #Step 2: Initialize s2 hashmap and map all the frequencies inside the sliding window
        s2_map = {}

        for i in range(len(s1)):
            char = s2[i]

            if char not in s2_map:
                s2_map[char] = 1
            else:
                s2_map[char] += 1
        
        if s2_map == s1_map:
            return True

        #Step 3: Now implement the logic for sliding window. 
        left = 0
        for right in range (len(s1), len(s2)):
            #bring in the new character
            right_char = s2[right]

            if right_char not in s2_map:
                s2_map[right_char] = 1
            else:
                s2_map[right_char] += 1
            
            left_char = s2[left]
            s2_map[left_char] -= 1
            if s2_map[left_char] == 0:
                del s2_map[left_char]
                
            left += 1
            if s1_map == s2_map: return True
            
            
        return False
