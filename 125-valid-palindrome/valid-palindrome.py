class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        my_str = ''.join(char.lower() for char in s if char.isalnum())

        return my_str == my_str[::-1]