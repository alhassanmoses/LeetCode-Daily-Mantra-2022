#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) < 2:
            return s
        
        left_pointer = 0
        right_pointer = len(s) - 1
        
        while left_pointer <= right_pointer:
            
            s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
            left_pointer += 1
            right_pointer -= 1

if __name__ == "__main__":
    
    sol = Solution()
    s = ["h","e","l","l","o"]
    sol.reverseString(s)
    print(s)