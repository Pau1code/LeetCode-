class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for num_i, i in enumerate(nums):
            if target - i not in dict:
                dict[i] = num_i
            else:
                return [dict[target - i], num_i]