"""Given an integer array with all positive numbers and no duplicates, find the
number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""


class Solution(object):
    """Class for solution."""
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        combos = [1] + [0] * target

        for i in range(1, target + 1):
            for num in nums:
                if num < i:
                    combos[i] += combos[i - num]
                elif num == i:
                    combos[i] += 1
                else:
                    break

        return combos[target]



##############################################################
# Testing...
s = Solution()
print "input [1, 2, 3] with target 4, expecting 7"
print "got >>>", s.combinationSum4([1, 2, 3], 4)
