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

    def twoSumAlt(self, nums, target):
        """
        :type nums:List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary with each num from the original list as a key,
        # and the compliment of that number as the value.  The compliment is
        # the target number - the number.  Also create a dict to hold the counts
        # of nums in case 2*num == target and num appears twice.
        compliments = {}
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            compliments[num] = target - num

        # Create variables to hold the two index values
        first_ind = int()
        sec_ind = int()

        # Check if the condition exists that num appears twice in list and
        # 2*num == target
        for num in counts:
            if counts[num] == 2 and num * 2 == target:
                first_ind = nums.index(num)
                sec_ind = nums[(first_ind + 1):].index(num) + first_ind + 1
                return [first_ind, sec_ind]

        # If the above condition is not true, find the num that has the
        # the compliment
        for num in compliments:
            if compliments[num] in nums:
                first_ind = nums.index(num)
                sec_ind = nums.index(compliments[num])
                return [first_ind, sec_ind]


#########################################################################
# Testing...
solution = Solution()
print "Expecting '[2, 3]', got...", solution.twoSum([1, 2, 3, 4], 7)
print "Expecting '[0, 3]', got...", solution.twoSum([25, 2, 3, 25, 67, 8], 50)

# testing the alternative function
print "Expecting '[2, 3]', got...", solution.twoSumAlt([1, 2, 3, 4], 7)
print "Expecting '[0, 3]', got...", solution.twoSumAlt([25, 2, 3, 25, 67, 8], 50)
