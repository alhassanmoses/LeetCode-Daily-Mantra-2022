class Solution:
    
    def removeDuplicates(self, nums):
        
        if len(nums) < 2:
            return len(nums)
        
        left_slide = 1
        right_slide = 1
        count = 1
        
        while right_slide < len(nums):
            if nums[right_slide] == nums[right_slide - 1]:
                right_slide += 1
                continue
                
            if nums[right_slide] != nums[right_slide - 1]:
                nums[left_slide] = nums[right_slide]
                right_slide += 1
                left_slide += 1
                count +=1
                
        return count

if __name__ == "__main__":
    
    sol = Solution()
    print(sol.removeDuplicates([1,1,2]))
    print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    