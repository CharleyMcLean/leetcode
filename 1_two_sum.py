class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Iterate through the list of nums
        for i in range(len(nums)):
            # We're looking for a number that, added to nums[i], will == target
            match = target - nums[i]
            # Check the rest of the list after index i
            if match in nums[(i + 1):]:
                # i is the index of the first number
                # To avoid repeating the same index (ex if target - num = num),
                # get the index of the match (looking at list starting with
                # i + 1), then adding i + 1 to that value to get the correct
                # index value of the entire list.
                return [i, nums[(i + 1):].index(match) + i + 1]

#########################################################################
# Testing...
solution = Solution()
print "Expecting '[2, 3]', got...", solution.twoSum([1, 2, 3, 4], 7)
print "Expecting '[0, 3]', got...", solution.twoSum([25, 2, 3, 25, 67, 8], 50)
