class Solution(object):
    # This is a DP problem. We don't need to print each
    # unique path. If we did we can do backtrack.
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Since this is m x n, we first instantiate
        # a 2d array of that size.

        num_ways = [[0 for x in range(m)]for y in range(n)]

        # Since the objective will always have a top entrance and
        # a left entrance, we will add those ways to get the ways
        # someone can enter our current cell.

        for rows in range(n):
            num_ways[rows][0] = 1

        for columns in range(m):
            num_ways[0][columns] = 1

        #print(num_ways)
        for rows in range(1,n):
            for columns in range(1,m):
                num_ways[rows][columns] = num_ways[rows-1][columns] + num_ways[rows][columns-1]

        return num_ways[-1][-1]
