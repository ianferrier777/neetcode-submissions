class Solution:
    # for "time = O(n²); space = O(1)" solution
    # def __init__(self):
    #     self.i = 0
    #     self.j = 1

    def hasDuplicate(self, nums: List[int]) -> bool:
        # time = O(n²); space = O(1)
        # if self.i >= len(nums) - 1:
        #     return False
        # elif nums[self.i] == nums[self.j]:
        #     return True
        # elif self.j == len(nums) - 1:
        #     self.i += 1
        #     self.j = self.i + 1
        #     return self.hasDuplicate(nums)
        # else:
        #     self.j += 1
        #     return self.hasDuplicate(nums)

        #####################################################

        # time = O(n); space (array modified in place) = O(1)
        # nums.sort()

        # for i, num in enumerate(nums):
        #     if i == len(nums) - 1:
        #         return False
        #     elif num == nums[i + 1]:
        #         return True

        #####################################################

        # time = O(log n); space O(n)
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)

        return False


        

