"""Find the contiguous subarray within an array (containing at least one number)
which has the largest product.

For example, given the array [2, 3, -2, 4],
the contiguous subarray [2, 3] has the largest product = 6.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxi = mini = result = nums[0]

        for i in range(1, len(nums)):
            possibilities = [(maxi * nums[i]), (mini * nums[i]), nums[i]]
            maxi = max(possibilities)
            mini = min(possibilities)
            result = max(maxi, result)

        return result


####################################################
# Testing...
solution = Solution()
print "Input [2, 3, -2, 4], expecting 6.  Got >>>", solution.maxProduct([2, 3, -2, 4])
print "Input [-2], expecting -2.  Got >>>", solution.maxProduct([-2])
print "Input [3, -1, 4], expecting 4.  Got >>>", solution.maxProduct([3, -1, 4])
print "Input [-2, 3, -4], expecting 24.  Got >>>", solution.maxProduct([-2, 3, -4])
print "Input [-4, -3, -2], expecting 12.  Got >>>", solution.maxProduct([-4, -3, -2])
