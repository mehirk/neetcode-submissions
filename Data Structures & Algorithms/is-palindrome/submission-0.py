class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumString = ""
        for i in s:
            if i.isalnum():
                alphanumString += i.lower()

        return alphanumString == alphanumString[::-1]