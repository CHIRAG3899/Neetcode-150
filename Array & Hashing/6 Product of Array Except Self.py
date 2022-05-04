#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
#You must write an algorithm that runs in O(n) time and without using the division operation.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]
#Example 2:
#
#Input: nums = [-1,1,0,-3,3]
#Output: [0,0,9,0,0]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. set up a base case if len(nums) < 2 to return 0
        if len(nums) < 2:
            return 0
        
        # 2. set up the answer array, as well as the left and right pointers, set all values to 1
        answer = [1 for _ in range(len(nums))]
        left = 1
        right = 1
        
        # 3. go thru the array, multiply the values in the answer array with the pointers first, and then get new values for left and right
        for i in range(len(nums)):
            answer[i] *= left
            answer[len(nums) - i - 1] *= right
            left *= nums[i]
            right *= nums[len(nums) - i - 1]
        
        # 4. return the answer array
        return answer

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp=[]
        product=1
        for i in nums:
            dp.append(product)
            product*=i
        product=1
        for i in range(len(nums)-1,-1,-1):
            dp[i]=dp[i]*product
            product*=nums[i]
        return dp