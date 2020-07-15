# We write the integers of A and B (in the order they are given) on two separate horizontal lines.

# Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

# A[i] == B[j];
# The line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

# Return the maximum number of connecting lines we can draw in this way.

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0]*len(A) for _ in range(len(B))]
        dp[0][0] = 1 if A[0] == B[0] else 0
        for index_i in range(1, len(dp)):
            dp[index_i][0] = dp[index_i-1][0]
            if A[0] == B[index_i]:
                dp[index_i][0] = 1
        for index_j in range(1, len(dp[0])):
            dp[0][index_j] = dp[0][index_j-1]
            if B[0] == A[index_j]:
                dp[0][index_j] = 1
        for index_i in range(1, len(dp)):
            for index_j in range(1, len(dp[0])):
                if A[index_j] == B[index_i]:
                    dp[index_i][index_j] = max(dp[index_i-1][index_j-1] + 1, max(dp[index_i-1][index_j], dp[index_i][index_j-1]))
                else:
                    dp[index_i][index_j] = max(dp[index_i-1][index_j-1], max(dp[index_i-1][index_j], dp[index_i][index_j-1]))
        return dp[len(B)-1][len(A)-1]
