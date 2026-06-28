class Solution:
    def thirdMax(self, a):
        a.sort()

        x = 1
        y = a[-1]

        for i in range(len(a) - 2, -1, -1):
            if a[i] != y:
                x += 1
                y = a[i]

            if x == 3:
                return y

        return a[-1]
