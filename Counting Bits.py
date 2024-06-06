class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []

        for a in range(0,n+1):
            count = 0
            a = bin(a)
            for i in a:
                if i == '1':
                    count += 1
            ans.append(count)
        
        return ans
