# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s = s.lower()
        
        if s == " " or len(s) < 2:
            
            return True
            
        
        s = "".join(s.split(' '))
        s = "".join(filter(str.isalnum, s))
        
        left_pointer = 0
        right_pointer = len(s) - 1
        
        while left_pointer < right_pointer:
            if s[left_pointer] == s[right_pointer]:
                
                left_pointer += 1
                right_pointer -= 1
                
            else:
                
                return False
            
        return True

if __name__ == "__main__":
    
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s))