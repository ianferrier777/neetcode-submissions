class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # time = O(n); space O(n)
        # nums_set = set()

        # for num in nums:
        #     if num in nums_set:
        #         return True
        #     else:
        #         nums_set.add(num)

        # return False

        #####################################################

        # time = O(n); space (array modified in place) = O(1)
        nums.sort()

        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                return False
            elif num == nums[i + 1]:
                return True
        
        return False



        

