class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Initialize two pointer, l at the start and r at the end of the string
        l, r = 0, len(s) - 1

        #Loop until the two pointers meet in the middle.
        while l < r:
            # Increment the left pointer if the current character is not alphanumeric.
            while l < r and not self.alphanum(s[l]):
                l += 1 
            # Decrement the right pointer if the current character is not alphanumeric.
            while l < r and not self.alphanum(s[r]):
                r -= 1

        # Compare the characters at the left and right pointers for equality,
            # after converting them to lowercase to ensure case-insensitivity.
            if s[l].lower() !=  s[r].lower():
                return False
            
            # Move the pointers closer to the middle.
            l += 1
            r -= 1
        
        # If all characters have been checked and matched, the string is a palindrome.
        return True

# is Palaindrome Helper function to determine if a character is alphanumeric.
    def alphanum(self, c):
        # Check if the ASCII value of 'c' is within the ranges of 'A'-'Z', 'a'-'z', or '0'-'9'.
        return (
            ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9")
        )

# Example of usage:
sol = Solution()
example_string = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(example_string))  # Output: True