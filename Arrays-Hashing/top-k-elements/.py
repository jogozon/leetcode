class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # make the number of occurences the index 
        # of the values
 
        # first get the count of each element
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # the largest this array needs to be is the size of num
        # b/c that's the max occurrences possible
        bucketArray = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            bucketArray[c].append(n)

        res = []
        # range of the max occurences, go backwards
        #                           start, stop, step
        for i in range(len(bucketArray) - 1, 0, -1):
            for n in bucketArray[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        