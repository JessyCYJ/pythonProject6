class Solution:
    def Fibonacci(self , n):
        #从0开始，第0项是0，第一项是12
        if n <= 1:
            print(n)
            return n
        a = 0
        b = 1
        sum = 0
        #因n=2时也为1，初始化的时候把a=0，b=1
        for i in range(2, n + 1):
        #第三项开始是前两项的和,然后保留最新的两项，更新数据相加
            sum = (a + b)
            a = b
            b = sum
        print(sum)
        return sum


xiaomu = Solution()
xiaomu.Fibonacci(n=0)