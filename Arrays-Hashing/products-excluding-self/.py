class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # get all the products before the index
        # get all the products after the index
        # multiply the two together

        # assume 1 if out of bounds
        res = [1] * (len(nums))
        for i in range(1, len(nums)):
            # in the first element the number stays what the value of 
            # the element is
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        print('output', res)
        for j in range(len(nums) - 1, -1, -1):
            # mutiply the prefix by the postfix
            res[j] *= postfix
            # adjust the postfix after multiplying to keep up
            postfix *= nums[j]
        return res


        # input -> 1  2  3  4
        # pre ->   1  2  6  24
        # post ->  24 24 12 4
        # res ->   24 12 8  6 
            
