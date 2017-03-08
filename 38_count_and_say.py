"""The count-and-say sequence is the sequence of integers beginning as
follows:
1, 11, 21, 1211, 1112221, ...
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, one 1" or 1211

Given an integer n, generate the nth sequence.
Note: the sequence of integers will be represented as a string.
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        current = str(1)

        if n == 1:
            return current
        
        temp = current[0] # for n = 2 --> temp = "1"
        nth = []
        count = 1
        for i in range(2, n + 1): #[2]
            for j in range(1, len(current)): 
                if current[j] == temp: #