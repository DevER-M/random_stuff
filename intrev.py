class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            temp=str(-x)[::-1]
            return int(str(f"-{temp}"))
        else:
            return int(str(x)[::-1])

sol=Solution()
print(sol.reverse(-123))