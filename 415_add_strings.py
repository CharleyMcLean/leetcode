"""Given two non-negative integers 'num1' and 'num2' represented as strings,
return the sum of 'num1' and 'num2'.
 - The length of both 'num1' and 'num2' is < 5100
 - Both 'num1' and 'num2' contains only digits '0-9'
 - Both 'num1' and 'num2' do not contain any leading zero
 - You must not use any built-in BigInteger library or convert the inputs
   to integer directly"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str

        Will come back and cleanup code with helper function.
        """
        # Check if both are zero
        if not num1 and not num2:
            return str(0)

        # Check if one of the numbers is zero
        if not num1:
            return num2
        if not num2:
            return num1

        # make num1 the larger number
        if len(num2) > len(num1):
            num1, num2 = num2, num1

        # reverse the numbers, map integer values to list.
        # if num1, num2 = '123', '19' then rev1, rev2 = [3, 2, 1], [9, 1]
        rev1, rev2 = map(int, num1[::-1]), map(int, num2[::-1])

        # iterate through the length of the shorter list (rev2)
        rev_added = []
        to_carry = int()

        if len(rev1) == len(rev2):
            for i in range(len(rev1) - 1):
                added = rev1[i] + rev2[i] + to_carry
                if added > 9:
                    rev_added.append(str(added % 10))
                    to_carry = added / 10
                else:
                    rev_added.append(str(added))
                    to_carry = 0
            rev_added.append(str(rev1[-1] + rev2[-1] + to_carry))

        else:
            for i in range(len(rev2)):
                added = rev1[i] + rev2[i] + to_carry
                if added > 9:
                    rev_added.append(str(added % 10))
                    to_carry = added / 10
                else:
                    rev_added.append(str(added))
                    to_carry = 0

            # Now account for the rest of the digits in the longer list (rev1)
            for j in range(len(rev2), len(rev1) - 1):
                added = rev1[j] + to_carry
                if added > 9:
                    rev_added.append(str(added % 10))
                    to_carry = added / 10
                else:
                    rev_added.append(str(added))
                    to_carry = 0

            rev_added.append(str(rev1[-1] + to_carry))

        # Items were added to the list as strings so that they could
        # be joined here (cannot use this to join ints.)
        return "".join(rev_added[::-1])


#########################################################################
# Testing...
solution = Solution()
print "'' and '', expecting '0', got...", solution.addStrings('', '')
print "'' and '1', expecting '1', got...", solution.addStrings('', '1')
print "'2', '', expecting '2', got...", solution.addStrings('2', '')
print "'9', '912', expecting '921', got...", solution.addStrings('9', '912')
print "'9', '99', expecting '108', got...", solution.addStrings('9', '99')
print "'9876', '3258, expecting '13134', got...", solution.addStrings('9876', '3258')
print "'9876', '13258', expecting '23134', got...", solution.addStrings('9876', '13258')
print "Result is correct type?", type(solution.addStrings('2', '1')) == str

