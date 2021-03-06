#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example 1:
# Input: 2
# Output: [0,1,1]

# Example 2:
# Input: 5
# Output: [0,1,1,2,1,2]

# Follow up:
# - It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# - Space complexity should be O(n).
# - Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
#
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # Ref: https://www.cnblogs.com/grandyang/p/5294255.html
        # Ref: https://blog.csdn.net/coder_orz/article/details/52063216
        result = []
        for i in range(0, num + 1):
            result.append(bin(i).count('1'))
        return result

if __name__ == '__main__':
    solution = Solution()
    print('expected=[0,1,1], actual={}'.format(solution.countBits(2)))
    print('expected=[0,1,1,2,1,2], actual={}'.format(solution.countBits(5)))
