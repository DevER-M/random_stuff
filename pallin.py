class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        rev_x=0
        temp=x
        while temp!=0:
            digit=temp%10
            rev_x=rev_x*10+digit
            temp//=10
        return True if rev_x==x else False
    

from collections import deque
class Solution2(object):
    def isPalindrome(self, x:int):
        if x < 0:
            return False
        
        d = deque(iter(x))
        
        while len(d) > 1:
            if d.popleft() != d.pop():
                return False
        
        return True

sol = Solution2()
print(sol.isPalindrome(121))