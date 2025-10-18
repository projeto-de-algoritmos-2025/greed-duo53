class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        n = len(slices) // 3

        # função pra resolver o caso linear (sem ser circular)
        def solve_linear(arr):
            m = len(arr)
            dp = [[0] * (n + 1) for _ in range(m + 1)]

            for i in range(1, m + 1):
                for j in range(1, min(i, n) + 1):
                    take = arr[i - 1] + (dp[i - 2][j - 1] if i >= 2 else 0)
                    skip = dp[i - 1][j]
                    dp[i][j] = max(skip, take)

            return dp[m][n]

        # ignora o primeiro ou o último pra quebrar o ciclo
        case1 = solve_linear(slices[1:])
        case2 = solve_linear(slices[:-1])

        # retorna o melhor resultado
        return max(case1, case2)
