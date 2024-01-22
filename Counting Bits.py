class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]

        for i in range(1, n + 1):
            # If the current number is odd (last bit is 1), add 1 to the count.
            if i % 2 == 1:
                dp.append(dp[i - 1] + 1)
            else:
                # If the current number is even, count of set bits is the same as for i/2.
                dp.append(dp[i // 2])

        # Return the final list
        return dp
