class Solution:
    def myPow(self, x: float, n: int) -> float:
        #base case
        if n==0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)
            
        #recursive case
        a=self.myPow(x, n//2)
        if n%2==0:
            return a*a
        else:
            return a*a*x
        