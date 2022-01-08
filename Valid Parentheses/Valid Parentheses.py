# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            
            return False
        
        if len(s) < 2:
            
            return False
        
        lookup = {')': '(' , '}': '{', ']' : '['}
        
        valid = False
        
        queue = []
        queue.append(s[0])
        
        for i in range(1,len(s)):
            
            val = s[i]
            
            if val in lookup:
                
                if len(queue) == 0:
                    
                    return False
                
                if lookup[val] != queue.pop():
                    
                    return False
                
            else:
                
                queue.append(val)
                
        return len(queue) == 0

if __name__ == "__main__":
    
    sol = Solution()
    s = "()"
    print(sol.isValid(s))