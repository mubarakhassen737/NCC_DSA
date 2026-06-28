class Solution:
    def plusOne(self, q):
        for w in range(len(q) - 1, -1, -1):
            if q[w] < 9:
                q[w] += 1
                return q
            q[w] = 0
        return [1] + q
