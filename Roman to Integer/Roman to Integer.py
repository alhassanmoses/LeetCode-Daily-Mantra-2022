# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/

class Solution:
    def romanToInt(self, s: str) -> int:
        
        look_up = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        if len(s) == 2:
                        
            if look_up[s[1]] > look_up[s[0]]:
                return look_up[s[1]] - look_up[s[0]]
                                       
            else:
                return look_up[s[1]] + look_up[s[0]]
                                            
        skip = False
        
        running_sum = 0
        
        for i in reversed(range(len(s))):
            
            if skip:
                    skip = False
                    continue
            
            if i == 0:
                
                running_sum += int(look_up[s[i]])
            else:

                if look_up[s[i]] > look_up[s[i - 1]]:

                    running_sum += look_up[s[i]] - look_up[s[i - 1]]
                    skip = True

                else:

                    running_sum += int(look_up[s[i]])
                
        return running_sum
                
                
                
if __name__ == "__main__":
    
    sol = Solution()
    s = "LVIII"
    print(sol.romanToInt(s))