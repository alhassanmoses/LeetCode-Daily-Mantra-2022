# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3:
            return []
        
        result = set()
        nums.sort()
        
        for offset in range(len(nums) - 2 ):
            
            left_pointer = offset + 1
            right_pointer = len(nums) - 1
        
            while left_pointer < right_pointer:

                sum = nums[offset] + nums[left_pointer] + nums[right_pointer]

                if sum == 0:

                    result.add((nums[offset], nums[left_pointer], nums[right_pointer]))
                    left_pointer += 1
                    right_pointer -= 1

                else:

                    if sum < 0:

                        left_pointer += 1

                    elif sum > 0:

                        right_pointer -= 1 
                        
                        
        if len(result) == 0:
            
            return []
                        
        else:
            rusult = filter(lambda i,j,k: i != j and i != j and i !=k, result)
            
            return result

if __name__ == "__main__":
    
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))