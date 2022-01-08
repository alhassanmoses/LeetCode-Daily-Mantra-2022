# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = {}
        
        for i in range(len(nums)):
            seeking = target - nums[i]
            if seeking in nums_dict:
                return [nums_dict[seeking], i]
            else:
                nums_dict[nums[i]] = i
                
            
if __name__ == "__main__":
    
    sol = Solution()
    nums = [2,7,11,15]
    print(sol.twoSum(nums, 9))