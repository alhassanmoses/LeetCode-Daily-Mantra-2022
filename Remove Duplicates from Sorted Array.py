class Solution:
    
    # def removeDuplicates(self, nums):
        
    #     if len(nums) < 2:
    #         return len(nums)
        
    #     current_dup_begining = 0
    #     dup_trace_active = False
        
    #     #for i in range(1, len(nums)):
    #     i = 1
    #     limit = len(nums)
    #     while i < len(nums): 
    #         print("Hi")
            
    #         if nums[i] == nums[i-1] and i < len(nums):
    #             print("Hello")
                
    #             if i == len(nums) - 1:
    #                 i = self.adjust_array(nums, current_dup_begining, i - 1)
    #                 return len(nums)
                
    #             if not dup_trace_active:
                    
    #                 dup_trace_active = True
    #                 current_dup_begining = nums[i]
    #                 i += 1
                    
    #         if dup_trace_active:
    #             dup_trace_active = False
    #             i = self.adjust_array(nums, current_dup_begining, i - 1)
            
    #         i += 1
        
    #     return len(nums)
                    
                    
    # # def flip_dup_trace_state():
    # #     self.dup_trace_active = !self.dup_trace_active
        
                    
    # def adjust_array(self, nums, current_dup_begining, current_dup_end):
    #     count = current_dup_end - current_dup_begining + 1
        
    #     while count > 0:
            
    #         nums.pop(current_dup_begining)
    #         count -= 1
            
    #     return current_dup_begining

    def removeDuplicates(self, nums):
        
        if len(nums) < 2:
            return len(nums)
        
        if len(nums) == 2 and (nums[0] == nums[1]):
            nums.pop()
            return 1
        
        current_dup_begining = None
        dup_trace_active = False
        
        #for i in range(1, len(nums)):
        i = 1
        while i < len(nums): 
            
            if nums[i] == nums[i-1]:
                              
                if not dup_trace_active:
                    
                    dup_trace_active = True
                    current_dup_begining = i
                    i +=1                    
                    
                if i == len(nums) - 1:
                    i = self.adjust_array(nums, i if not current_dup_begining else current_dup_begining, i)
                    return len(nums)
                    
            if dup_trace_active:
                dup_trace_active = False
                i = self.adjust_array(nums, current_dup_begining, i - 1)
                continue
            
            i += 1
        
        return len(nums)
                    
                    
    # def flip_dup_trace_state():
    #     self.dup_trace_active = !self.dup_trace_active
        
                    
    def adjust_array(self, nums, current_dup_begining, current_dup_end):
        # print(f"{current_dup_begining} {current_dup_end}")
        count = current_dup_end - current_dup_begining + 1
        
        while count > 0:
            
            nums.pop(current_dup_begining)
            count -= 1
            
        return current_dup_begining

if __name__ == "__main__":
    
    sol = Solution()
    # sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    sol.removeDuplicates([1,1,2])